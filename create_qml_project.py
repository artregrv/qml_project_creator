import os

print(os.getcwd())

cmakelists_content = "\
cmake_minimum_required(VERSION 3.27)\n\
\n\
list(APPEND CMAKE_PREFIX_PATH \";/Users/arturegorov/Qt/6.7.2/macos\")\n\
\n\
project(test_project)\n\
\n\
set(CMAKE_AUTOMOC ON)\n\
set(CMAKE_AUTORCC ON)\n\
\n\
find_package(Qt6 COMPONENTS REQUIRED Core Gui Qml)\n\
\n\
add_executable(${PROJECT_NAME}\n\
    main.cpp\n\
)\n\
\n\
target_link_libraries(${PROJECT_NAME}\n\
    PRIVATE\n\
        Qt6::Core\n\
        Qt6::Gui\n\
        Qt6::Qml\n\
)\n\
qt_add_qml_module(${PROJECT_NAME}\n\
    URI\n\
        testModule\n\
    QML_FILES\n\
        Main.qml\n\
)\n\
"

main_qml_content = "\
import QtQuick.Controls\n\
\n\
ApplicationWindow {\n\
    width: 720\n\
    height: 480\n\
    visible: true\n\
}\n\
"

main_cpp_content = "\
#include <QGuiApplication>\n\
#include <QQmlApplicationEngine>\n\
\n\
int main(int argc, char *argv[])\n\
{\n\
    QGuiApplication application(argc, argv);\n\
\n\
    QQmlApplicationEngine engine;\n\
    engine.loadFromModule(\"testModule\", \"Main\");\n\
\n\
    return application.exec();\n\
}\n\
"

build_script_content = "\
#!/bin/bash\n\
\n\
mkdir -p build\n\
cd build\n\
cmake ../test\n\
cmake --build .\n\
\n\
./test_project\n\
"

def createCmakeFile(directory):
    fileName = os.path.join(directory, "CMakeLists.txt")
    file = open(fileName, "w")
    file.write(cmakelists_content)
    file.close()    

def createMainQml(directory):
    fileName = os.path.join(directory, "Main.qml")
    file = open(fileName, "w")
    file.write(main_qml_content)
    file.close()    

def createMainCpp(directory):
    fileName = os.path.join(directory, "main.cpp")
    file = open(fileName, "w")
    file.write(main_cpp_content)
    file.close()    


def createBuildScript(directory):
    fileName = os.path.join(directory, "run.sh")
    file = open(fileName, "w")
    file.write(build_script_content)
    file.close()    

    os.system("chmod +x run.sh")


testDir = os.path.join(os.getcwd(), "test")

if (not os.path.exists(testDir)):
    os.mkdir(testDir)

createCmakeFile(testDir)
createMainQml(testDir)
createMainCpp(testDir)
createBuildScript(os.getcwd())
