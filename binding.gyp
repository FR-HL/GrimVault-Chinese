{
  "targets": [
    {
      "target_name": "native",
      "product_dir": "<(module_root_dir)/src/native/.build",
      "sources": [
        "src/native/async.cpp",
        "src/native/logger.cpp",
        "src/native/main.cpp",
        "src/native/ocr.cpp",
        "src/native/screen.cpp",
        "src/native/util.cpp",
        "src/native/wgc.cpp",
        "src/native/windows.cpp",
        "vendor/screen_capture_lite/src_cpp/windows/GetMonitors.cpp",
        "vendor/screen_capture_lite/src_cpp/windows/GetWindows.cpp",
        "vendor/screen_capture_lite/src_cpp/windows/ThreadRunner.cpp",
        "vendor/screen_capture_lite/src_cpp/windows/DXFrameProcessor.cpp",
        "vendor/screen_capture_lite/src_cpp/windows/GDIFrameProcessor.cpp",
        "vendor/screen_capture_lite/src_cpp/windows/GDIMouseProcessor.cpp",
        "vendor/screen_capture_lite/src_cpp/ScreenCapture.cpp",
        "vendor/screen_capture_lite/src_cpp/SCCommon.cpp",
        "vendor/screen_capture_lite/src_cpp/ThreadManager.cpp"
      ],
      "dependencies": [
        "<!(node -p \"require('node-addon-api').targets\"):node_addon_api"
      ],
      "include_dirs": [
        "<(module_root_dir)/node_modules/node-addon-api",
        "<(module_root_dir)/vcpkg_installed/x64-windows/include",
        "<(module_root_dir)/vcpkg_installed/x64-windows/include/opencv4",
        "<(module_root_dir)/vendor/screen_capture_lite/include",
        "<(module_root_dir)/vendor/screen_capture_lite/include/windows"
      ],
      "configurations": {
        "Release": {
          "msvs_settings": {
            "VCCLCompilerTool": {
              "ExceptionHandling": 1,
              "AdditionalOptions": [
                "/EHsc",
                "/Zi",
                "/Zc:__cplusplus",
                "/bigobj",
                "/await"
              ],
              "Optimization": 3,
              "FavorSizeOrSpeed": 1,
              "InlineFunctionExpansion": 2,
              "WholeProgramOptimization": "true",
              "StringPooling": "true",
              "EnableFunctionLevelLinking": "true",
              "EnableEnhancedInstructionSet": 2,
              "DebugInformationFormat": 3,
              "RuntimeLibrary": 2
            },
            "VCLinkerTool": {
              "LinkTimeCodeGeneration": 1,
              "GenerateDebugInformation": "true",
              "AdditionalLibraryDirectories": [
                "<(module_root_dir)/vcpkg_installed/x64-windows/lib"
              ]
            }
          }
        }
      },
      "msvs_settings": {
        "VCCLCompilerTool": {
          "AdditionalOptions": [
            "/Zc:__cplusplus",
            "/bigobj",
            "/await",
            "/EHsc"
          ]
        }
      },
      "defines": [
        "WINRT_LEAN_AND_MEAN",
        "NOMINMAX",
        "WIN32_LEAN_AND_MEAN"
      ],
      "libraries": [
        "d3d11.lib",
        "d3dcompiler.lib",
        "DirectXTex.lib",
        "DirectXTK.lib",
        "dxgi.lib",
        "dxguid.lib",
        "dwmapi.lib",
        "onnxruntime.lib",
        "opencv_core4.lib",
        "opencv_dnn4.lib",
        "opencv_highgui4.lib",
        "opencv_imgcodecs4.lib",
        "opencv_imgproc4.lib",
        "opencv_photo4.lib",
        "Shcore.lib",
        "windowsapp.lib"
      ]
    }
  ]
}