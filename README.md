## Extract-i18n Translate Service

Provides a localized translation interface, uses the `deep_translator`` library, can support multiple translation engines, if you need to change, see the `deep_translator [DOCUMENTATION](https://pypi.org/project/deep-translator/)


### RUN in local

```
./start.sh
```

### RUN in docker

```
docker-compose up -d
```

### Request Format

```
curl http://localhost:8081/translate?to=en&text=你好
```