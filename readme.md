docker build --build-arg GIT_COMMIT=$(git rev-parse HEAD) -t jmbaejo12/axe-test-web-server:$(git rev-parse HEAD) .
