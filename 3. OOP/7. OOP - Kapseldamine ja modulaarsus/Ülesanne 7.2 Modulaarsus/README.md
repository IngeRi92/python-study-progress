Ülesanne 7.2: Modulaarsus

Vaatleme lihtsat kooli infosüsteemi, milles on kool, õpilased ja kursused. Õpilastele saab kursuste eest hindeid panna.

Alustame sellest, et olgu meil kood, mis pole üldse modulaarne. Seda võib võtta kui näidet, mida süsteemis soovitakse teha. Aga väga keeruline luua uusi õpilasi ja seejärel võtta välja õpilaste järjestust keskmise hinde järgi.

```Python
if __name__ == '__main__':
    # school has student who study
    students = []

    # it also has different courses/subjects
    courses = []

    # each student has name and unique id
    student1 = {'name': 'John Smith', 'id': '1'}
    student2 = {'name': 'Mary Lee', 'id': '2'}

    # let's add two students to university
    students.append(student1)
    students.append(student2)

    # let's see all the students:
    print(students)

    # let's add some courses
    course1 = "Math"
    course2 = "Physics"
    courses.append(course1)
    courses.append(course2)

    # each student should also have grades for courses
    # let's add a dict of grades to each student
    # the key is the subject, the value is the grade
    for student in students:
        # an empty list in the beginning
        student['grades'] = {}

    # student1 got 4 and 5
    student1['grades'][course1] = 4
    student1['grades'][course2] = 5

    # student2 got 5
    student2['grades'][course1] = 5

    # new student joins the university
    students.append({'name': 'Cocoo Turner', 'id': '3', 'grades': {}})

    # the new students gets some grades
    students[-1]['grades'][course1] = 3
    students[-1]['grades'][course2] = 5

    # print out students and their average grades, from the highest grade to lowest
    ordered_students = sorted(students, key=lambda s: sum(s['grades'].values()) / len(s['grades']), reverse=True)
    for student in ordered_students:
        print(student['name'], sum(student['grades'].values()) / len(student['grades']))

    # get average grades for each subject
    for course in courses:
        course_grades = []
        for student in students:
            for course_name, grade in student['grades'].items():
                if course_name == course:
                    course_grades.append(grade)
        print(course, sum(course_grades) / len(course_grades))
```

Selles koodinäites on kasutatud õpilase andmete hoidmiseks sõnastikku. Selliselt on vead väga kerged tekkima, kui näiteks kogemata kirjutad sõnastiku võtme valesti. Samuti uut õpilast luues peame teadama, millised võtmed tuleb ära väärtustada. Kui näiteks otsustame lisada õpilasele uue välja "vanus", siis peame väga palju koodi ära muutma.

Antud ülesande eesmärk on sama funktsionaalsusega kood kirjutada klassidega ringi nii, et selle kasutamine oleks mugavam. Alustame sellest, et loome kolm klassi: School (kool), Student (õpilane), Course (kursuse/õppeaine). Et eriliselt rõhutada modulaarsust, siis loome ise klassi eraldi faili, vastavalt: school.py, student.py ja course.py. Igas failis (moodulis) on üks klass. Kuigi tavapäraselt pole mõtet asju nii põhjalikult jagada (eriti, kui kood ei ole väga pikk), siis siin näite jaoks teeme selle põhjalikult läbi.

Ülesande jaoks tuleb realiseerida järgmised klassid ja vastav funktsionaalsus.

### Course (kursus/õppeaine)

See klass hoiab infot ühe õppeaine kohta.

Loo järgmised meetodid:

- `def __init__(self, name: str)` - konstruktor, kuhu saab kaasa anda kursuse nime. Arvatavasti on vaja siin konstruktoris luua info ka selle jaoks, et hoida õpilaste hindeid.
- `def get_grades(self) -> list[tuple[Student, int]]` - meetod tagastab järjendi õpilaste tulemustest. Järjendi iga element on ennik (tuple), kus esimene element on õpilase objekt ja teine on tema hinne. Hindeid pannakse School klassis oleva meetodiga add_student_grade(). Mõistlik on kursuse klassi lisada mingi abistav meetod, millega hinnet lisada.
- `def get_average_grade(self) -> float` - tagastab kursuse keskmise hinde. Ehk siis keskmine kõikidest sellele kursusel antud hinnetest. Kui hindeid pole, siis tagastab meetod -1.
- `def __repr__(self)` - tagastab "ilusa" sõne kuju antud objektist, ehk tagastab kursuse nime. Kuigi **str** meetodi realiseerimine annaks suuresti sama tulemuse, siis **repr** eelis on see, et ka listi ja enniku jm andmestruktuuri sees näidatakse objekti vastavalt määratud sõne kujul.

### Student (õpilane)

Klass hoiab ühe õpilase infot.

Loo järgmised meetodid:

- `def __init__(self, name: str)` - konstruktor, kuhu saab kaasa anda õpilase nime. Siin on vaja luua muutuja(d) õpilase hinnete hoidmiseks. Lisaks tuleb luua muutuja õpilase id jaoks, mille väärtust alguses peab olema None.
- `def set_id(self, id: int)` - õpilasele määratakse unikaalne identifikaator. Kui identifikaator on juba määratud, siis teist korda seda üle kirjutada ei saa (sellisel juhul lihtsalt ignoreeritakse uue väärtuse lisamist)
- `def get_id(self) -> int` - tagastab õpilase identifikaatori
- `def get_grades(self) -> list[tuple[Course, int]]` - tagastab järjendi õpilase tulemustest. Iga element on ennik (tuple), mille esimene element on kursuse objekt ja teine element on hinne sellel kursusel. Hindeid pannakse School klassis oleva meetodiga add_student_grade(). Mõistlik on õpilase klassi lisada mingi abistav meetod, millega hinnet lisada.
- `def get_average_grade(self)` - tagastab õpilase keskmise hinde. Kui õpilasel hindeid pole, tagastab meetod -1.
- `def __repr__(self) -> str` - tagastab objekti sõnekuju. Siin klassis tagastab õpilase nime.

### School (kool)

Kool koondab kokku õpilased ja kursused.

Loo järgmised meetodid:

- `def __init__(self, name)` - konstruktor, kuhu saab kaasa anda kooli nime. Kooli nimi tuleb salvestada muutujasse self.name. Lisaks on mõistlik luua üks muutuja õpilaste ja üks muutuja kursuste hoidmiseks.
- `def add_course(self, course: Course)` - kursus lisatakse kooli. Kui selline kursus on juba olemas, siis seda teistkordselt ei lisata.
- `def add_student(self, student: Student)` - õpilane lisatakse kooli. Kui selline õpilane on juba olemas, siis teda teistkordselt ei lisata. Ühtlasi kui õpilane lisatakse kooli, siis määratakse talle unikaalne id (set_id() meetod õpilasel).
- `def add_student_grade(self, student: Student, course: Course, grade: int)` - lisatakse hinne õpilasele konkreetse kursuse eest. Hinne lisatakse ainult siis, kui õpilane on selles koolis ja kursus on selles koolis olemas. Hinne peaks minema ka õpilase ja kursuse külge (selleks, et nende kaudu saada hindeinfot kätte). Seega siin on mõistlik välja kutsuda vastavalt õpilasel ja kursusel mingeid oma loodud meetodeid, mis salvestavad hinded nende objektide külge. Siin ei pea arvestama olukorraga, kui lisatakse hinne kursusele, kus juba on hinne (sellist olukorda ei testita). Kui on soovi, võid proovida sellises olukorras uut hinnet ignoreerida või kirjutad vana üle. Hinde väärtust kontrollima ei pea. See on täisarv vahemikus 1-5 (kaasa arvatud).
- `get_students(self) -> list[Student]` - tagastab õpilaste järjendi. Elemendid on Student objektid ning elemendid on järjendis nende lisamise järjekorras.
- `get_courses(self) -> list[Course]` - tagastab kursuste järjendi. Elemendid on Course objektid ning elemendid on järjestatud nende lisamise järjekorras.
- `def get_students_ordered_by_average_grade(self) -> list[Student] `- tagastab õpilaste järjendi järjestatuna keskmise hinde järgi nii, et eespool on õpilane, kelle keskmine hinne on kõrgem. Siin ei pea midagi erilist tegema õpilastega, kelle keskmine hinne on sama (need võivad jääda samasse järjekorda).

Anname kaasa ka ühe näite, milline kood võiks töötada nende klassidega:

```Python
from school import School
from student import Student
from course import Course


if __name__ == '__main__':
    school = School("Awesome School")
    student1 = Student("John Smith")
    student2 = Student("Mary Lee")

    school.add_student(student1)
    school.add_student(student2)

    # we cannot add one student twice
    school.add_student(student1)

    print(len(school.get_students()))  # 2

    course1 = Course("Math")
    course2 = Course("Physics")
    school.add_course(course1)
    school.add_course(course2)

    # we cannot add one course twice
    school.add_course(course1)

    print(len(school.get_courses()))  # 2

    school.add_student_grade(student1, course1, 4)
    school.add_student_grade(student1, course2, 5)
    school.add_student_grade(student2, course1, 5)

    student3 = Student("Cocoo Turner")

    # cannot add grades to the student who is not in the school
    school.add_student_grade(student3, course1, 5)

    print(len(student3.get_grades()))  # 0

    school.add_student(student3)
    school.add_student_grade(student3, course1, 3)
    school.add_student_grade(student3, course2, 5)

    print(len(student3.get_grades()))  # 2

    print(student3.get_grades())  # [(Math, 3), (Physics, 5)]

    print(course1.get_grades())  # [(John Smith, 4), (Mary Lee, 5), (Cocoo Turner, 3)]

    print("Students ordered by average grade:")
    print(f"{'Student':>15}: avg grade")
    print("-" * 30)
    for student in school.get_students_ordered_by_average_grade():
        print(f"{student.name:>15}: {student.get_average_grade():.2f}")

    print()
    print("Course average grades")
    for course in school.get_courses():
        print(f"{course.name:>10}: {course.get_average_grade():.2f}")
```

## Vihjed

### School

School klassis on mõistlik luua konstruktoris muutujad self.students = [] ja self.courses = [], kuhu salvestada vastavalt õpilased ja kursused.

Kuna õpilaste lisamisel tuleb meile unikaalne identifikaator lisada, võib mõelda sellist lahendust, kus konstruktoris luuakse mingi muutuja, mis hoiab viimast id väärtust. Näiteks self.\_next_id = 1. Kui õpilane lisatakse, määratakse see väärtus tema id-ks (set_id meetodiga). Seejärel saab next id väärtust suurendada. Seda saab iga õpilane unikaalse id. Üks variant oleks mõelda ka sellele, et id väärtuseks saab panna self.students listi pikkuse. See antud ülesande puhul toimiks. Aga kui õpilasi saaks koolist eemaldada, siis tekiks probleem. Kui näiteks koolis on kaks õpilast: A ja B. Nende id-d oleks vastavalt 1 ja 2. Kui nüüd eemaldatakse A õpilane ja lisatakse uus õpilane C, siis talle läheks väärtuseks 2. Aga B id on ka 2 ja seega see ei sobi.

Õpilase ja kursuse lisamisel tuleb eelnevalt kontrollida, ega sellist objekti juba pole. Näiteks õpilase puhul: if student not in self.students - alles siis võib lisamise teha.

Hinde lisamise puhul tuleks kontrollida, kas õpilane ja kursus on koolis olemas. Seejärel oleks mõistlik näiteks õpilasele ja kursusele lisada meetodid add_grade vms. Neid meie tester ei nõua. Aga need on selleks, et saaksid mugavalt lisada hinde. Vaata allpool vihjeid, kuidas seal neid meetodeid võiks luua.

get_students_ordered_by_average_grade puhul saab kasutada sarnast järjestamist nagu algses koodinäites oli. Kuna seal oli tegemist sõnastikega, siis see võrdluse osa tuleks objektide puhul natuke teistmoodi. Kuna meil on õpilase objektil olemas keskmise hinde meetod, saabki kirjutada võrdluse osasse: key=lambda student: student.get_average_grade()

### Student

Õpilase konstruktoris tuleks luua väli id jaoks, näiteks self.id = None. Selle algne väärtus peab olema None. Kui hiljem set_id meetodiga hakatakse id-d lisama, saab kontrollida, kas praegune väärtus on tühi. Kui on tühi, siis saab uue väärtuse lisada. Kui aga pole tühi, siis ei tee meetod midagi. Kontrollida saab: if self.id is None.

Hinnete salvestamise jaoks on vaja teada nii kursust kui selle hinnet. Kuna get_grades() meetod peab tagastama järjendi ennikutest, kus esikohal on kursus ja siis hinne, siis võib neid andmeid täpselt sellisel kujul ka hoida. Saab konstruktoris luua: self.grades = []. Hinde lisamiseks saab luua eraldi meetodi, näiteks add_grade(self, course: Course, grade: int). Kui lisatakse hinne, siis self.grades.append((course, grade)). Sedasi saab hiljem get_grades() meetodis mugavalt tagastada return self.grades. Siin ei pea muretsema sellepärast, et sama õppeaine võib mitu hinnet saada. Kui on huvi, võid proovida lahendada nii, et korduva aine hinde puhul seda ignoreeritakse või kirjutatakse üle (õpilane n-ö parandas oma tulemust).

Keskmise hinde arvutamisel tuleb summeerida kõik õpilase hinded ja jagada läbi hinnete arvuga. Kui hindeid pole, siis hinnete arv on 0 ja tekiks 0-ga jagamine. Seepärast tuleb eraldi kontrollida, et kui hindeid pole, tuleb tagastada -1.

### Course

Kursuse puhul tuleb samamoodi salvestada sellel kursusel antud hinded. Mõistlik on teha seda analoogselt õpilase klassiga. Võib salvestada ennikutena self.grades = []. Ja lisada eraldi meetod add_grade, mis lisab hinde ennikuna: self.grades.append((student, grade)).

Keskmise hinde arvutamisel saab jällegi teha sarnaselt õpilase klassiga.
