<!--
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** rm-workspace-api, __fschindler__, fabian.schindler@eox.at
-->

<!-- PROJECT SHIELDS -->
<!--
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/EOEPCA/rm-registration-api">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Registration API</h3>

  <p align="center">
    Template for developing an EOEPCA Service
    <br />
    <a href="https://github.com/EOEPCA/rm-registration-api"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/EOEPCA/rm-registration-api">View Demo</a>
    ·
    <a href="https://github.com/EOEPCA/rm-registration-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/EOEPCA/rm-registration-api/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Testing](#testing)
- [Documentation](#documentation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/EOEPCA/rm-registration-api)

Here's a blank template to get started:
**To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`rm-workspace-api`, `__fschindler__`, `fabian.schindler@eox.at`

### Built With

- FastAPI
- Redis

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

To develop this service both `docker` and `docker-compose` is required.


### Installation

```
docker-compose up
```

### Testing

- `make test` runs the unit tests
- `make lint` runs the code lints

## Documentation

The component documentation can be found at https://eoepca.github.io/rm-registration-api/.

<!-- USAGE EXAMPLES -->

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

### Running the template service

Just execute the run task in Gradle

```sh
./gradlew run
```

### Upgrading Gradle Wrapper

Change the version number in the `build.gradle` wrapper task then run:

```sh
./gradlew wrapper --gradle-version=4.10.2 --distribution-type=bin
```

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/EOEPCA/rm-registration-api/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the Apache-2.0 License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Fabian Schindler - [@__fschindler__](https://twitter.com/__fschindler__) - fabian.schindler@eox.at

Project Link: [https://github.com/EOEPCA/rm-registration-api](https://github.com/EOEPCA/rm-registration-api)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- README.md is based on [this template](https://github.com/othneildrew/Best-README-Template) by [Othneil Drew](https://github.com/othneildrew).

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/EOEPCA/rm-registration-api.svg?style=flat-square
[contributors-url]: https://github.com/EOEPCA/rm-registration-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/EOEPCA/rm-registration-api.svg?style=flat-square
[forks-url]: https://github.com/EOEPCA/rm-registration-api/network/members
[stars-shield]: https://img.shields.io/github/stars/EOEPCA/rm-registration-api.svg?style=flat-square
[stars-url]: https://github.com/EOEPCA/rm-registration-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/EOEPCA/rm-registration-api.svg?style=flat-square
[issues-url]: https://github.com/EOEPCA/rm-registration-api/issues
[license-shield]: https://img.shields.io/github/license/EOEPCA/rm-registration-api.svg?style=flat-square
[license-url]: https://github.com/EOEPCA/rm-registration-api/blob/master/LICENSE
[product-screenshot]: images/screenshot.png
