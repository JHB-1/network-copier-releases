# ClipBridge downloads

[Download the latest release](https://github.com/JHB-1/network_copier-releases/releases/latest)

Windows x64: download **clipbridge.exe**, run it, then sign in to Google in your browser. No companion DLL or configuration file is required beside the executable. Windows may show a SmartScreen warning because the EXE does not have an Authenticode certificate.

트레이 메뉴의 **언어 / Language**에서 한국어·영어·시스템 기본값을 선택할 수 있습니다. 설정과 Google 인증 정보는 사용자 프로필에 보관되며 배포 파일에 포함되지 않습니다.

Version 0.3.0+ checks this repository for signed updates. Newer builds are downloaded in the background and restart only when transfers and pending clips are finished. Failed startup triggers rollback. Existing pre-updater installations need this EXE installed once manually.

If an older build reports **Update helper did not become ready**, exit ClipBridge and replace its EXE with the latest download once. Settings and Google login remain. The fixed updater shows download progress, verification, waiting reasons and restart results under **Check for updates**.

기존 버전에서 **Update helper did not become ready**가 나오면 앱을 종료하고 최신 EXE로 한 번 직접 교체하세요. 설정과 로그인은 유지됩니다. 수정본은 **업데이트 확인**에서 진행률·검증·설치 대기 이유·재시작 결과를 표시합니다.

This repository contains release binaries, signed update metadata, LGPL relink materials, and the publication workflow. Application source is maintained privately. Official downloaded updates require valid signatures; running a locally relinked EXE does not require a developer signature. Release signing is separate from Windows Authenticode.

Qt Core/Gui/Widgets are statically linked under LGPLv3 on Windows. Ordinary use needs only the EXE. The matching `clipbridge-lgpl-relink.tar.gz` contains application objects/libraries, exact Qt source, licenses, and rebuild instructions for replacing Qt. No user settings, login tokens, or private signing keys are included. Disable automatic updates to retain your locally modified Qt build.

Settings: `%LOCALAPPDATA%\ClipBridge\config.toml`. Set `[updates] enabled = false` to disable automatic checks. Menu **Check for updates** performs an explicit check and installs an available update. Data directory and Google login survive replacement.

Google OAuth access may require the account to be registered as a test user while the application is in testing mode. Download availability does not grant access to another user's Google Drive.
