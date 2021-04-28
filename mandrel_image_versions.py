import re

def main():
    mav_re = re.compile('MAVEN_VERSION=([\d\.]*)')
    jav_re = re.compile('JAVA_PACKAGE=.*?([\d]+)')
    man_re = re.compile('MANDREL_VERSION=.*?(\d+\.\d+)')

    mav_vers = ""
    jav_vers = ""
    man_vers = ""

    with open("maven-jdk-mandrel-builder.Dockerfile", "r") as f:
        for line in f:
            if result := mav_re.search(line):
                mav_vers = result.group(1)
            elif result := jav_re.search(line):
                jav_vers = result.group(1)
            elif result := man_re.search(line):
                man_vers = result.group(1)

    tag = f'{mav_vers}-{jav_vers}-{man_vers}'
    print(tag)

    return tag

if __name__ == "__main__":
    main()
