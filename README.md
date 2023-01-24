# Foreign Verbs

Spaced reptition of verbs in a foreign language.

## Description

A script that sends you at specific intervals (`cron` job) the conjugation of a verb.

For example, I want to be send daily via email the conjugation of a verb in Russian (the language I am learning) in the present tense. The verb is randomly selected from a list of verbs that I have already studied. Basically, it is a form of spaced repetition.

PS: I also want to apply what I recently learned in [Version Control with Git](https://www.coursera.org/learn/version-control-with-git) and start using long-term branches (`main` and `develop`) and feature branches.

## Getting Started

### Build with

- **Python 3**

### Dependencies

- [MSMTP](https://wiki.archlinux.org/title/msmtp)

### Installing


### Executing program


## Help


## Authors


## Version History

### v0.10

My first thought was designing a relational database for storing the different tenses of hundreds verbs, maybe even for multiple languages. That is overkill. I only have 2 dozen of verbs, so a quick and dirty proof of concept for a dozen verbs stored in flat files, makes more sense.

- [x] prepare a dozen flat files with verbes conjugated in the present tense
- [x] read the list and randomly pick one file/verb
- [x] send content of file via email using `msmtp`

## License

This project is licensed under the **MIT License** - see the LICENSE.md file for details

## Acknowledgments
