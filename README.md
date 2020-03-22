Скрипты для сравнение форматов сериализации данных в языке python3. Рассматриваются форматы csv, json, protobuf, pickle.

Lxc контейнер:
```bash
lxc init ubuntu:18.04 blog-2
lxc config set blog-2 raw.idmap "both $UID 1000"
lxc config device add blog-2 project disk source=$PWD path=/home/ubuntu/blog-2
lxc start blog-2
lxc exec blog-2 -- sudo --login --user ubuntu
cd blog-2
```

Установка зависимостей:
```bash
./deps.sh
```

Запуск скрипта:
```bash
./main.py --data-size 10000 --iterations 1000
```

Результатом скрипта будет benchmark времени сериализации / десериализации и размер данных в сериализованном формате. В папке results записывается сериализованный результат. Десериализованный результат записывается в формате csv.
