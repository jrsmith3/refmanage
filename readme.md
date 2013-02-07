Motivation
==========

The objective of this project is to develop a system that streamlines
the process of scholarship so that my expert time and energy are not
inefficiently wasted on inane, time consuming tasks. This document
describes the process of scholarship and writing, and separates the
parts of this process which are time consuming but unavoidable from the
parts that can be automated or delegated to a machine. Finally, I
describe a system and a set of tools that streamline the process of
scholarship and writing.

There are several routine tasks that are part of the work of science.
Just like a musician must practice scales or a basketball player must
practice free-throws, a scientist must practice scholarship and write
about his results. Scholarship is the practice of understanding one’s
work in the context of what has been reported in the literature. Among
other things, scholarship involves learning, reading, and writing. A
large part of scholarship involves wrangling the literature: the massive
set of published information. Organizing and searching the literature is
a science unto itself, but fortunately a number of tools and systems
have been developed to make dealing with the literature a manageable
endeavor even by a non-expert. Some of these tools are libraries and
librarians, the internet, Google, Web of Science, PACS, digital object
identifiers (DOI), international standard book number (ISBN), personal
recommendations and my professional/social network, structures for
formatting bibliographic data (RIS, bibtex), posts on the internet, and
even *The Literature* itself, in the form of lists of citations within
manuscripts as well as what I call "forward references” - works that
cite a particular manuscript. Ultimately, the objective of a scientist
is to contribute to humanity’s understand of how the universe works.
Practically, the scientist does this by contributing to the literature
by linking his work into this vast web of information.

For what it’s worth, I’m defining “manuscript” as an individual unit of
*The Literature* - usually a book or scientific article but sometimes a
post on the internet.

Background, Related Systems, and Use Cases
==========================================

A detailed description of the processes I use for reading and writing
are beyond the scope of this document, but I will need to give an
overview of these processes in order to show where the refmanage package
fits.

Writing
-------

I use latex to prepare my own manuscripts, and therefore I use bibtex to
manage all of the citation metadata. I have found that a monolithic
database is better than individual bibliographic databases for each
manuscript I prepare. To manage the bibliographic database, I have been
using the package Tellico because it can import and export many
different formats (bibtex, RIS, etc.).

Practically speaking, I collect a physical stack of manuscripts while I
am writing, and to make a citation I will match the bibtex key of a
particular manuscript to a particular location within the document.
Latex then uses this map as well as the bibtex database to generate the
proper citation indexing and the bibliography for the manuscript.

The takeaway here is that unique identifiers for each item in the
bibliographic database are critically important. These UIDs need to
exist as the bibtex key within the bibliographic database, and the UID
should be physically printed somewhere on the hardcopy of the
manuscript. In this way I can simply copy the printed UID into the
proper location of my manuscript and latex and bibtex will do all of the
heavy lifting.

Searching and Reading the Literature
------------------------------------

If writing is the back-end process of the refmanage system, the
searching and reading to learn are the front-end processes. why do I
need to read? I think there are at least two reasons. First, I need to
understand what has already been reported in the literature so that I
can convince myself of the novelty of my own work. Spanning the subspace
of the literature that is relevant to my work is the only way to achieve
that goal and amounts to collecting all of the relevant manuscripts. The
second reason to search the literature is to actually learn things. For
example, I once did a literature search to understand how atomic
hydrogen interacted with the Si (100) surface. For both of these
activities, the process I use to deal with the literature is the same.

From a practical standpoint, I have developed a process to deal with the
literature. I do not know what particular manuscripts contain the
information I need beforehand, so I typically start with keyword
searches in a search engine to generate a kernel of manuscripts on a
particular subject. In addition, I sometimes inherit this kernel from
others either by receiving one or many manuscripts on a topic. I will
read through this kernel, marking citations within this material that
seem appropriate to look at later. Also it sometimes seems appropriate
to look for the forward references for a particular manuscript. At the
end of this process I have an understanding of the landscape and a set
of manuscripts that is a representation of this understanding.

There are a few important takeaways from this discussion. First, my
process for searching the literature results in a list of manuscripts;
some of these manuscripts are relevant and some are not. It is mentally
more expensive to sort the list according to relevance than it is to
just include everything I’ve found in my bibliographic database.
Therefore I should just import everything I find into my system. Second,
I prefer to read a hardcopy of a manuscript as opposed to reading the
HTML/PDF/etc. version on my computer.

Specification and Requirements
==============================

In this section I will describe all of the requirements the refmanage
system will have to meet based on the systems it supports, and I will
describe the cases this system will not address.

Requirements
------------

The main goal of this reference management system is to facilitate
writing and reading by automating and removing the tedium of managing
the collection of manuscripts I have read. Based on the discussion of
writing and reading in the previous section, there will be three main
components of this system.

-   Physical incarnations of manuscripts: printouts, books, etc.

-   Electronic incarnations of manuscripts: PDFs, webpages, etc.

-   A database with bibliographic data for each individual manuscript.

What kinds of things will the system manage? In short, anything I can
cite in a paper. The two main entries are other scientific papers,
books, and sections or pages of books.

Here is a list of requirements.

1.  For each manuscript, there should be a single and individual
    physical incarnation, a single and individual electronic
    incarnation, and a single entry in the database. Single means no
    duplicates, and individual means no concatenation of multiple
    manuscripts into a single unit. Subsections of individual
    manuscripts may exist in the database, such as page ranges within a
    book, but should not typically exist as physical or electronic
    incarnations. This requirement means that each file should contain
    one and only one complete manuscript, etc.

2.  It should be a rare occurrence for me to manually key in an entry to
    the database or to import/maintain any part of the system by hand.

3.  Importing an arbitrary number of items into the system should be
    easy and automatic. The database item, electronic incarnation, and
    physical incarnation should all be generated simultaneously. At the
    time of import, all database, electronic, and physical items should
    be marked, labeled, and linked appropriately and automatically.

4.  As a default, a single command should import items into the system.
    However, sufficient granularity should exist to execute individual
    steps of the process.

5.  Collecting and processing new manuscripts should occur in a fashion
    similar to GTD.

6.  The system should not be overly complex, difficult to use, or
    difficult to set up.

7.  The system should handle exceptions (information that isn’t a book
    or paper) gracefully.

8.  The system should not import duplicates. If the importer notices a
    duplicate, a warning should be thrown. Manually manipulating the
    system is the only way to thwart this functionality.

9.  This system should be robust against changes made by third parties
    (e.g. publishers, the developer of Tellico, etc.). In other words,
    critical parts of the process or toolchain should not break simply
    because a third party changes functionality.

10. This system will tend to import more than I need. The economics work
    out such that it is better to get something that I don’t need rather
    than to need something but not have it. There is a negligible cost
    to importing superfluous items, I don’t typically know what is
    important at the outset of collecting and reading manuscripts, and
    there is an additional mental cost to organizing things according to
    relevance after I have read them.

11. Making changes to the system should not break backwards
    compatibility. In other words, I should be able to make dramatic
    changes to the system or toolchain and I should still be able to
    build my old manuscripts using latex without rewriting them.

12. Scripts and programs which are part of the system should be tidy in
    their business. Locations of temporary files should be explicit and
    cleanup of temporary files should be sensible.

13. Options controlling the behavior of scripts and programs should be
    contained in a config file. This config file should be in some kind
    of structured plaintext format like XML. For example, the location
    of the folder containing the electronic incarnations of manuscripts,
    the location of the database, etc. should all be explicitly
    specified in the config file.

14. Given any individual hardcopy, I should not have to query the
    database in order to cite the manuscript in my own manuscript.
    Therefore, the bibtex key should appear on the hardcopy.

15. It should be easy to locate any particular hardcopy. I shouldn’t
    have to spend hours searching through a stack of papers or books to
    find what I’m looking for.

16. I should be able to easily batch print a set of manuscripts. After
    searching the literature, I usually end up with a set of `~10`
    manuscripts in PDF format. I should be able to execute at most a
    single command to have them all appear at the printer.

17. I need a system to manage hardcopies during the reading process.

18. Electronic incarnations of manuscripts should be located in one flat
    folder in the filesystem.

19. The filename of the electronic incarnation of the manuscript should
    uniquely identify the manuscript contained therein.

20. The files representing electronic incarnations of manuscripts should
    be searchable because then the collection of files would be a
    knowledgebase and tools like spotlight could be used to search
    through the set of files.

21. Each file representing the electronic incarnation of a manuscript
    should contain structured bibliographic metadata identical to the
    metadata in the database.

22. For each item in the database, the bibliographic data should be
    complete.

23. The database should have a pointer to the physical location of the
    hardcopy

24. The database should have a link to the electronic incarnation in the
    filesystem.

25. The database needs to be able to export to bibtex. Having Tellico as
    part of the toolchain satisfies this condition.

Non-goals
---------

This version will not support the following features:

1.  Maintenance on the existing bibliographic database and/or system.

General Design
==============

This section contains descriptions, block diagrams, workflows, flow
diagrams, etc which describe how the refmanage system works. It will
also contain a subsection on how the system can be gracefully upgraded.

Organization of the System
--------------------------

In this section I will describe how the entire refmanage system is
organized as well as what third party elements the system depends on. A
number of components and systems already exist which the refmanage
system can leverage, some of these pre existing components are
international standards.

It is critical that each item in the system has a unique identifier.
Things would be even better if that UID was also an international
standard. Nearly every manuscript that exists in the literature is
uniquely identified with a DOI. Moreover, every book is uniquely
identified with an ISBN. These UIDs will be used as the bibtex keys of
the manuscript. For papers, the DOI will be marked on the physical
incarnation so I can easily cite a manuscript I’m holding in a document
I’m writing. Every book has the ISBN printed somewhere on the book
itself, therefore I can easily cite a book in hand while writing a
document. I will use the ISBN-13 if it is printed on the book, otherwise
I’ll use the ISBN-10. Sometimes I will need to only refer to a
subsection of a book. In this case, I will use a bibtex key of the
book’s ISBN with the following suffix appended: `_startpage-endpage`.

Besides books and papers, I will deal with other items I need to cite on
a case-by-case basis, preferring a published international standard UID
as the bibtex key. If it turns out that I routinely need to deal with a
particular category of items, I will specify it in this document at a
later date.

The refmanage system is made up of a physical component, an electronic
component, and a database. The physical component includes books and
papers that have been printed and bound with staples or binder clips.
The books will be located on a bookshelf in my office. Since the number
of books I own is small, a glance at the bookshelf should be all that’s
necessary to find what I need. A more robust organizational system can
be developed as necessary. On the other hand, the number of papers
printed out will be large and they will therefore require more
organization. It is best to think of these papers organized as a stack
or an indexed list: as I acquire new papers, they wind up on the bottom
of the stack. The DOI is not the right way to organize the physical
stack since new papers may need to be placed within the stack as opposed
to just the end. Papers will be marked with and organized according to
their Tellico ID (described below), which is simply a unique incremental
index for each item in the database. Papers will be stored in three-ring
binders marked with the range of Tellico IDs. In this way, searches can
be executed on the knowledgebase of files and the corresponding physical
incarnation of the manuscript can be easily found. The database can be
used to find a Tellico ID given a DOI, title, author, etc. Finally,
subsets of the physical incarnations of papers can be removed and easily
replaced without disturbing the organization of the system.

The electronic component of the refmanage system is a folder on the
filesystem containing electronic incarnations of manuscripts, mostly PDF
files. The name for each file will be the DOI/ISBN of the corresponding
manuscript. The filename will exactly match the bibtex key in the
database except as follows: the DOI will be modified such that the slash
character (/) is replaced with double underscore characters (`__`). This
construction avoids disallowed characters in filenames.

Ultimately, I will need a single monolithic bibtex file to reference in
my latex documents. However, the bibtex format is difficult to work with
programmatically and I would prefer to deal with an XML file or a real
database like sqlite. I have been using Tellico for a number of years to
manage my bibliographic database, and it is the right tool to continue
using moving forward. The Tellico database file is a compressed XML file
which can easily be manipulated using python. Tellico itself has a
number of command line options which can also be accessed via python.
Tellico can import and export in all the formats I need, and has a front
end for easy database management. The Tellico database file should be
located in the same directory as the electronic incarnations of the
manuscripts. Tellico can export its database as a bibtex file; that
bibtex database should be located in the same folder as everything else.
Each entry in the Tellico database is indexed with a unique integer
called the Tellico ID, and every new item added to the database gets the
next incremented number. Since the physical incarnations of manuscripts
are ordered as an indexed list, assigning each item a unique integer
results in the easiest organization. Tellico also provides functionality
to link the location of the electronic incarnation of a manuscript in
the filesystem to the database entry. This hyperlinking will be done to
match the database entries to their corresponding electronic
incarnations.

Currently all of the electronic files are located in
`~/Documents/library` which is a good location to stay with, but the
location should be a configurable option.

To recap, using the DOI/ISBN as the bibtex key and insisting that UID is
marked on the physical incarnation means that a physical pile of papers
and books are sufficient to generate the citations in a document. Using
these UIDs means that any physical incarnation of a document is
unambiguously linked to the rest of the literature since the DOI and
ISBN are international standards for identification. The DOI/ISBN scheme
also means that the physical incarnation points both to the electronic
incarnation and a database item, and vice-versa (in all directions).
Finally, all of the physical incarnations can be easily sorted using the
Tellico ID. This sorting provides a way to quickly find a specific
physical incarnation of a manuscript within the stack.

Most publishers’ websites provide both a PDF file containing the
manuscript and the bibliographic metadata in a downloadable format
either as a bibtex file or RIS file. Additionally, Google Scholar
provides the bibliographic metadata as a .bib file. These citation files
generally come with some default bibtex key, but also the DOI. I would
prefer to use the citation file from the publisher’s website, but the
bibtex file from Google is also acceptable. Using publisher provided
bibliographic metadata is the best way to ensure the data is complete
and since the data is already there, these files will eliminate errors
that occur via hand-transcription.

I will use python to write all of the scripts and programs necessary for
automation.

Workflow
--------

The following describes a general, iterative workflow. This process may
need to be repeated more than once in order to get all of the references
into the database along with printouts, etc. In this section, databases
in memory are denoted by `\emph`, and filenames are denoted by `\verb`.

1.  The process starts either with a set of bibliographic metadata files
    (.bib, .ris, etc.) or with a tellico database file of items to be
    imported into the master database. The user would typically acquire
    the bibliographic metadata files by manually downloading them from
    the internet. The tellico database file may come from a step in this
    process because the initial database items were missing their DOI,
    PDFs for import database files couldn’t be found, or for some other
    reason.

2.  The user executes the importer. Default functionality is to look in
    the present directory for all bibliographic metadata files, but a
    command line switch can be used to specify a tellico database file
    located within the filesystem. If no existing tellico database file
    was specified, the importer looks at the present directory and
    generates a tellico database (*import*) by importing all of the
    citation files.

3.  The importer steps through the items in *import* and looks at each
    to see if each has a DOI. If not, the importer pops that item off
    into a new tellico database, *no-doi*. At the end of this operation,
    the importer throws a warning and saves `no_doi.tc` to the disk.

4.  The importer checks the items remaining in *import* to see if there
    are any duplicates by comparing DOIs. If so, the importer prunes
    *import* such that there are only singletons, and throws a warning.
    The importer saves the list of items with duplicates to a tellico
    database file on the disk: `import_dups.tc`.

5.  The importer opens the master database (*master*) and looks to see
    if any of the items in *import* are already in *master*. If so, the
    importer throws a warning, pops all of the duplicates out of
    *import*, and saves the list of duplicates to the disk:
    `master_dups.tc`.

6.  The importer steps through the remaining items in *import*. For each
    item, the importer searches for a pdf file with filename =
    `<modified DOI>.pdf`. The directory containing the PDFs defaults to
    pwd, but can also be specified via a switch on the command line when
    the importer is called. If the importer finds this file, it moves
    the file to the library folder (specified in the preferences file).
    If the importer cannot find the file locally, it uses the DOI and
    DOI resolver to attempt to download the file from the web. If the
    file is successfully downloaded, the importer renames the file to
    `<modified DOI>.pdf` and places it in the library folder. If the
    importer cannot download the PDF in this way, it pops the entry out
    of *import* into another tellico database, *no-pdf*. Once all the
    items in *import* have been dealt with, if there are items in
    *no-pdf*, the importer throws a warning and saves the list to the
    disk: `no_pdf.tc`. A command line switch can be used to keep copies
    of PDFs in the specified directory (they are moved to the library
    directory instead of copied by default)

7.  The importer steps through *import* and `no_pdf.tc` if it exists and
    does the following to each item in the database:

    -   Changes the bibtex key to the DOI.

    -   Changes the local URL to `<library dir> + <modified DOI>.pdf`.

    -   Changes the URL to `dx.doi.org/<DOI>`.

8.  The importer saves `import.tc` to the disk.

9.  The importer imports *import* into *master*.

10. The importer steps through the list of newly imported items and does
    the following for each PDF corresponding to the item.

    -   Watermarks every page of the PDF with the DOI and tellico ID.

    -   Embeds bibliographic metadata into the PDF file.

    -   OCRs the PDF if necessary.

    -   Sends the PDF to the printer. Depending on the printer and the
        page count of the PDF, 3-hole punch paper is selected and the
        top left corner is stapled. Specific options are specified in
        the preferences file. This option to print the PDFs can be
        suppressed by a switch on the command line.

11. The importer regenerates the master bibtex database file from
    *master* and prints stats about the import as well as the state of
    the present database.

12. The importer cleans up files according to defaults and options
    specified on the command line. These options are discussed below.

The importer should produce the following list of things once it has
finished:

1.  (OPTIONAL) A tellico database file of items that were missing their
    DOI: (`no_doi.tc`). This problem can be resolved by opening the file
    in tellico and manually fixing the DOIs. Once the DOIs are fixed,
    the importer can be executed again with `no_doi.tc` specified on the
    command line as the tellico database to import and everything should
    work.

2.  (OPTIONAL) A tellico database file whos items were missing the
    corresponding PDFs either because they weren’t found in the
    filesystem or because they weren’t downloadable from the internet
    (`no_pdf.tc`). This problem will have to be resolved manually. If
    the user locates the PDFs, the importer can be run once again using
    `no_pdf.tc` as the database to import. Otherwise `no_pdf.tc` can
    simply be manually imported into `master.tc` since the bibtex key,
    URL, etc. are already set properly.

3.  (deleted by default) A tellico database file containing all of the
    items that were imported (`import.tc`). A command line switch can be
    set to prevent deletion of this file.

4.  (OPTIONAL, deleted by default) A tellico database file of items that
    were duplicates within the original list (`import_dups.tc`). A
    command line switch can be set to prevent deletion of this file.

5.  (OPTIONAL, deleted by default) A tellico database file of items that
    were duplicates of items from the master database
    (`master_dups.tc`). A command line switch can be set to prevent
    deletion of this file.

6.  Leftover citation files in the original directory. Possibly some
    PDFs will be leftover in the original directory as well as other
    files that were irrelevant to the refmanage operation.

If the importer runs without generating items for 1 or 2, everything in
the import directory can be safely deleted. Therefore, the importer will
delete everything in this directory by default unless a switch on the
command line is used.

### Files associated with this program

-   `.refmanage`: configuration file.

-   `refmanage.py` and associated files: executable.

-   `master.tc`: master database.

### What’s in the config file?

-   Location of the library. Defaults to `~/Documents/library`.

-   User defined defaults for command-line switches.

-   Suppress certain behavior, e.g. don’t OCR incoming PDFs.

### Command line switches

-   Keep `import.tc`.

-   Keep `import_dups.tc`.

-   Keep `master_dups.tc`.

-   Don’t delete anything in the original directory upon successful
    completion.

-   Location of tellico database file to ue used as import instead of
    bibliographic metadata files in pwd.

-   Locaiton of PDFs to import (not in present directory).

Upgrading and evolution
-----------------------

All systems must evolve in order to handle changing requirements. My
hope is that I can capture much of the functionality I need with this
first version, but it is prudent to make the system flexible to handle
changes.

Consider the following: when I first started using tellico to handle my
references, I had a custom scheme to name bibtex keys: a, b, m, etc. for
article, book, manual, then a four-digit number that I incremented for
each new entry. At some point I got sick of keying in new bibtex keys
and changing filenames manually, so I just started using whatever bibtex
key came with the bibtex file I got from the publisher’s website. Now I
realize that DOI and ISBN are the best to use for bibtex keys (more on
that later). To maintain consistency, I should change all of the
database items’ bibtex keys, but that would break compatibility with old
versions of manuscripts.

I’ve already had lots of ideas on how to improve this thing like
inserting metadata into the PDFs themselves, overlaying DOI, tellico ID,
etc. on the PDFs themselves, etc. This system needs to be able to deal
with those updates without breaking. Some of these issues can be solved
by my version control system.

What’s left
-----------

Here are some lists of possible errors or user input during runtime.

-   First run: what if `master.tc`, etc doesn’t exist?

Additional thoughts
-------------------

-   bibxml

-   clean up current master.tc

-   do I need to keep copies of the pdf as downloaded from the
    publisher?

-   can I integrate this workflow/program even more with the internet
    (connotea/bibsonomy) or tellico? In other words, have a browser
    button that grabs bib data and pdf.

-   BibTeXML and Pybtex are probably better for database storage than
    bibtex.

-   BibTeXML: both Pybtex and tellico can parse this kind of file.

-   I would like covers and first pages as images for all the entries in
    the database. Scanning, pdftk, and imagemagik convert can make this
    dream a reality.

Maintenance tasks
-----------------

The following list are actions that I know I’d like to do, but should be
included as auxiliary functionality (if at all).

-   Is the bibtex key = DOI?

-   Does every entry have a DOI/ISBN/UID?

-   Does every entry have URL = `dx.doi.org/<DOI>`?

-   Is the local URL like for every entry correct, or is the target not
    there?

-   Are there files int eh library that do not have entries in the
    database?

-   Is the filename for each file in the library correct as modified
    DOI?

-   Are all the PDFs in the library OCRd?

-   Do all the PDFs in the library have the bibliographic metadata
    embedded?

-   Do all the PDFs int eh library have the DOI and tellico ID
    watermarked on all the pages?


