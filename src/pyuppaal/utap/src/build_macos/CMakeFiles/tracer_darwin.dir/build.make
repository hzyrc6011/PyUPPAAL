# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.27.7/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.27.7/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/taco/Desktop/GitRepo/tracer_custom/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/taco/Desktop/GitRepo/tracer_custom/src/build_macos

# Include any dependencies generated for this target.
include CMakeFiles/tracer_darwin.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/tracer_darwin.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/tracer_darwin.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/tracer_darwin.dir/flags.make

CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.o: CMakeFiles/tracer_darwin.dir/flags.make
CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.o: /Users/taco/Desktop/GitRepo/tracer_custom/src/tracer_custom.cpp
CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.o: CMakeFiles/tracer_darwin.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/taco/Desktop/GitRepo/tracer_custom/src/build_macos/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.o -MF CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.o.d -o CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.o -c /Users/taco/Desktop/GitRepo/tracer_custom/src/tracer_custom.cpp

CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/taco/Desktop/GitRepo/tracer_custom/src/tracer_custom.cpp > CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.i

CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/taco/Desktop/GitRepo/tracer_custom/src/tracer_custom.cpp -o CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.s

# Object files for target tracer_darwin
tracer_darwin_OBJECTS = \
"CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.o"

# External object files for target tracer_darwin
tracer_darwin_EXTERNAL_OBJECTS =

tracer_darwin: CMakeFiles/tracer_darwin.dir/tracer_custom.cpp.o
tracer_darwin: CMakeFiles/tracer_darwin.dir/build.make
tracer_darwin: CMakeFiles/tracer_darwin.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/taco/Desktop/GitRepo/tracer_custom/src/build_macos/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable tracer_darwin"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/tracer_darwin.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/tracer_darwin.dir/build: tracer_darwin
.PHONY : CMakeFiles/tracer_darwin.dir/build

CMakeFiles/tracer_darwin.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/tracer_darwin.dir/cmake_clean.cmake
.PHONY : CMakeFiles/tracer_darwin.dir/clean

CMakeFiles/tracer_darwin.dir/depend:
	cd /Users/taco/Desktop/GitRepo/tracer_custom/src/build_macos && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/taco/Desktop/GitRepo/tracer_custom/src /Users/taco/Desktop/GitRepo/tracer_custom/src /Users/taco/Desktop/GitRepo/tracer_custom/src/build_macos /Users/taco/Desktop/GitRepo/tracer_custom/src/build_macos /Users/taco/Desktop/GitRepo/tracer_custom/src/build_macos/CMakeFiles/tracer_darwin.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/tracer_darwin.dir/depend

