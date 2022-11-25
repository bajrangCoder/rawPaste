from django.apps import AppConfig
from django.utils import timezone


class PastesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pastes'
    APPLICATION_NAME = "rawPaste"
    SECRET_KEY_LENGTH = 6
    USER_KEY_LENGTH = 12
    SECRET_KEY_CHOICES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    USER_KEY_CHOICES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$&+/*!?~%^"
    FIFTEEN_MINUTES = "15min"
    ONE_HOUR = "1hr"
    ONE_DAY = "1d"
    ONE_WEEK = "1w"
    ONE_MONTH = "1mon"
    SIX_MONTH = "6mon"
    ONE_YEAR = "1y"
    STYLES = ['default', 'emacs', 'friendly', 'friendly_grayscale', 'colorful', 'autumn', 'murphy', 'manni', 'material', 'monokai', 'perldoc', 'pastie', 'borland', 'trac', 'native', 'fruity', 'bw', 'vim', 'vs', 'tango', 'rrt', 'xcode', 'igor', 'paraiso-light', 'paraiso-dark', 'lovelace', 'algol', 'algol_nu', 'arduino', 'rainbow_dash', 'abap', 'solarized-dark', 'solarized-light', 'sas', 'staroffice', 'stata', 'stata-light', 'stata-dark', 'inkpot', 'zenburn', 'gruvbox-dark', 'gruvbox-light', 'dracula', 'one-dark', 'lilypond', 'nord', 'nord-darker', 'github-dark']
    LANGUAGES = [
        ('abap', 'ABAP'),
        ('ada', 'Ada'),
        ("applescript", "AppleScript"),
        ("arduino", "Arduino"),
        ("bash", "Bash"),
        ("bat", "Batchfile"),
        ("c", "C"),
        ("clojure", "Clojure"),
        ("cmake", "CMake"),
        ('cobol', 'COBOL'),
        ("coffee-script", "CoffeeScript"),
        ("common-lisp", "Common Lisp"),
        ("console", "Console/Bash Session"),
        ('control', 'Debian Control file'),
        ('cpp', 'C++'),
        ("csharp", "C#"),
        ("css", "CSS"),
        ("cuda", "CUDA"),
        ('cython', 'Cython'),
        ("d", "D"),
        ("dart", "Dart"),
        ("delphi", "Delphi"),
        ("diff", "Diff"),
        ("django", "Django/Jinja"),
        ("docker", "Docker"),
        ("elixir", "Elixir"),
        ("erlang", "Erlang"),
        ('fortran', 'Fortran'),
        ('fsharp', 'FSharp'),
        ("go", "Go"),
        ("handlebars", "Handlebars"),
        ("haskell", "Haskell"),
        ("html", "HTML"),
        ("html+django", "HTML + Django/Jinja"),
        ('html+php', 'HTML+PHP'),
        ("ini", "INI"),
        ("ipythonconsole", "IPython console session"),
        ("irc", "IRC logs"),
        ("java", "Java"),
        ("js", "JavaScript"),
        ("json", "JSON"),
        ("jsx", "JSX/React"),
        ('jsp', 'Java Server Page'),
        ('julia', 'Julia'),
        ('koka', 'Koka'),
        ("kotlin", "Kotlin"),
        ("less", "LessCSS"),
        ('live-script', 'LiveScript'),
        ("lua", "Lua"),
        ("make", "Makefile"),
        ("matlab", "Matlab"),
        ('md', 'markdown'),
        ('mysql', 'MySQL'),
        ("nginx", "Nginx configuration file"),
        ('nim', 'Nimrod'),
        ("numpy", "NumPy"),
        ("objective-c", "Objective-C"),
        ('objective-c++', 'Objective-C++'),
        ("perl", "Perl"),
        ('perl6', 'Perl6'),
        ("php", "PHP"),
        ("postgresql", "PostgreSQL SQL dialect"),
        ('postscript', 'PostScript'),
        ('powershell', 'PowerShell'),
        ("python", "Python"),
        ('python3', 'Python 3'),
        ('qbasic', 'QBasic'),
        ('qml', 'QML'),
        ("rb", "Ruby"),
        ('rhtml', 'RHTML'),
        ("rst", "reStructuredText"),
        ("rust", "Rust"),
        ("sass", "Sass"),
        ('scala', 'Scala'),
        ("scss", "SCSS"),
        ("sol", "Solidity"),
        ("sql", "SQL"),
        ("swift", "Swift"),
        ('tcl', 'Tcl'),
        ("tex", "TeX"),
        ('text', 'Text only'),
        ('ts', 'TypeScript'),
        ("typoscript", "TypoScript"),
        ('vb.net', 'VB.net'),
        ("vim", "VimL"),
        ("xml", "XML"),
        ("xslt", "XSLT"),
        ("yaml", "YAML"),
        ('zephir', 'Zephir')
    ]