/**
 * Native module loader - loads the C++ addon for screen capture,
 * tooltip detection (DNN), and window event hooks.
 */

import electron from 'electron';
import { join } from 'node:path';
import { RESOURCES, ROOT, SOURCE } from './config.js';
import { logger } from './logger.js';

const { app } = electron;

// Native binaries are placed outside 'resources' to avoid Electron asar interception
let NATIVE_DIR;

if (app.isPackaged) {
  NATIVE_DIR = join (app.getAppPath (), '..', '..', 'native');
} else {
  NATIVE_DIR = join (SOURCE, 'native', '.build');
}

// Add DLL directory to PATH so native module can find its dependencies
process.env.PATH = `${NATIVE_DIR};${process.env.PATH}`;

// Load native module via dlopen (bypasses asar virtual filesystem)
let native = { exports: {} };
process.dlopen (native, join (NATIVE_DIR, 'native.node'));
native = native.exports;

// OCR model paths (PaddleOCR for text recognition)
let ocrModelPath, ocrDictPath, onnxModelPath, debugPath;

if (app.isPackaged) {
  ocrModelPath = join (NATIVE_DIR, 'models', 'paddleocr', 'latin_PP-OCRv5_mobile_rec.onnx');
  ocrDictPath = join (NATIVE_DIR, 'models', 'paddleocr', 'latin_pp_ocrv5_dict.txt');
  onnxModelPath = join (NATIVE_DIR, 'models', 'tooltip.onnx');
  debugPath = join (NATIVE_DIR, '..', 'debug');
} else {
  ocrModelPath = join (ROOT, 'models', 'paddleocr', 'latin_PP-OCRv5_mobile_rec.onnx');
  ocrDictPath = join (ROOT, 'models', 'paddleocr', 'latin_pp_ocrv5_dict.txt');
  onnxModelPath = join (ROOT, 'models', 'tooltip.onnx');
  debugPath = join (ROOT, 'debug');
}

let onMessageCallback = (level, message) => {
  logger [level] (`[Native] ${message}`);
};

// Initialize native screen capture and OCR engine
let success = native.initialize (
  ocrModelPath,
  ocrDictPath,
  onnxModelPath,
  onMessageCallback,
  debugPath
);

if (!success) {
  logger.error ('Native OCR initialization failed - Chinese OCR service will handle text recognition.');
}

let {
  getTooltip,
  getActiveWindow,
  getGameWindow,
  startWindowHooks,
  stopWindowHooks
} = native;

export {
  getTooltip,
  getActiveWindow,
  getGameWindow,
  startWindowHooks,
  stopWindowHooks
};
