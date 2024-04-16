# python-text-classification

N-gram text classification for large corpus

## Included

- [ ] Process large files
- [x] Test cases
- [x] Docker support


## Running locally

### Local Python version (3.12)

```sh
pyenv local
pyenv activate
```

### Executing script

```sh
python ngrams.py some-large-text.txt

# OR

cat some-large-text.txt | python ngrams.py
```

### Using with Docker

```sh
docker build . -t ngrams
docker run -i --rm ngrams < ./texts/mobydick.txt
cat ./texts/mobydick.txt | docker run -i --rm ngrams
```

## Running Tests

```sh
python tests.py
```
