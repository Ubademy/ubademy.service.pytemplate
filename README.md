# ubademy.service.courses
[![codecov](https://codecov.io/gh/Ubademy/ubademy.service.courses/branch/master/graph/badge.svg?token=T726IGKKWO)](https://codecov.io/gh/Ubademy/ubademy.service.courses) [![Tests](https://github.com/Ubademy/ubademy.service.courses/actions/workflows/test.yml/badge.svg)](https://github.com/Ubademy/ubademy.service.courses/actions/workflows/test.yml) [![Linters](https://github.com/Ubademy/ubademy.service.courses/actions/workflows/linters.yml/badge.svg)](https://github.com/Ubademy/ubademy.service.courses/actions/workflows/linters.yml) [![Deploy](https://github.com/Ubademy/ubademy.service.courses/actions/workflows/delpoy.yml/badge.svg)](https://github.com/Ubademy/ubademy.service.courses/actions/workflows/delpoy.yml)

## Run

``` bash
docker build . -t <image_name>

docker run -p <machine_port>:8000 <image_name>
```

## Tests
``` bash
make test
```

## Reformat
``` bash
make fmt
```

## Lint
``` bash
make lint
```
