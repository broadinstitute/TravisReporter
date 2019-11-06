# TravisReporter
Python script to report build errors to github from travis ( pre-alpha )

This is a small project which is used as a fast test bed for the Reporter.py script.  
This is a script which when run on travis in a pull request can be used to report uploaded log locations in a github comment.

It's specifically designed for use with [GATK](https//www.github.com/broadinstitute/gatk) but could be made more flexible for other projects.

### Usage
```
travis.yml:

export GITHUB_API_KEY=<github api key with public_repo permissions>
python Reporter.py <log url>
```
