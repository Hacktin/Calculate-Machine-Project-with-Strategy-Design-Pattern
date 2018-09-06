# Calculate-Machine-Project-with-Strategy-Design-Pattern
Design Pattern Example Trial from Phyton



1)Strateji Dizayn Paterni Nedir?
Strateji dizayn patterni, bir ata algoritma ailesi(soyut sınıf da denilebilir) oluşturup diğer nesil olan algoritma ailelerine(gerçek sınfılar ya da miras alan sınıflar da diyebiliriz) ise atadan aldıkları temel algoritma yapısı üzerinden değişiklikler yapabilmesini olanak sağlar.
Basit bir örnek verecek olursak:Matematik işlemleri yapabileceğimiz bir sınıfımızı(soyut sınıf ya da ata sınıf)düşünelim ve kendisinin temel bir metodu var.Bu metot işlemi yaptığına dahil bir çıktı veriyor diyelim ve hatta zahmet edilirse Phyton'daki Math modülünü kullanarak için metotları ve elle yazabileceğimiz toplama,çıkarma vb. dört işlemleri de metotumuza yazabiliriz.Ama tüm işlemleri bir sınıfa yüklemektense dağıtık bir mantıkla çalışmak yani  belli görevleri yapabilecek başka sınıflar oluşturulup o sınıfları genel soyut sınıftan miras almak daha mantıklı olacaktır ve bu da aynı zamanda Nesne yönelimli programlamanın nimetlerinde de faydalanmamızı sağlayacaktır.
Zaten genel olarak dizayn patternlerinde de amaç:Nesne yönelimli programlama sunduğu soyutlama tekniklerini kullanarak kod tekrarını,kullanıcı tarafıyla irtibata geçildiğinde bağımlı sınıf kullanımını önler.Özellikle bağımlı sınıftan kurtulma mantığı da dizayn patternleri arasında ismi yer alan meşhur Depency İnjection dizayn patternidir.Aşağıdaki kodlarda da bir Depency İnjection kodu yazmış bulunmaktayım.Aşağıda kodların yanlarına vs. açıklama da yapmış bulunmaktayım.İsterseniz şimdi kodlarımıza bakalım :)


##import math --Matematik işlemleri için Phyton'da kullanılan modülümüzdür--

class Mathematical:--İşte soyut veya ata sınıfımız.Burada yazdığımız metotlar ve özellikleri miras olarak verdiğimiz sınıflarda da kullanabilmemize olanak sağlacak-- **Burada bu sınıfın içinde de abc modülünü kullanarak metotları soyutlayabilirdim ama bilmiyorum burada normal bir şekilde sınıfımızı oluşturmuşum.**

    def __init__(self, sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2



    def OperationofMath(self):
        print("Operation completed")



class Squart(Mathematical):--Karekök sınıfımızızdır ve bu sınıf parantez içinde ata sınıf yazılarak Karekök sınıfı Mathematical sınıfından miras almış olur.**Miras alması sayesinde ata sınıftaki sayi1 ve sayi2 değerleri ile OperationofMath metodunu kullanabilmektedir ve OperationofMath metodu burada da farklı bir şekilde yazılmış**

    def __init__(self,sayi1,sayi2):
        super().__init__(sayi1,sayi2) --Super metodu genel olarak Squart sınıfa ait yapıcı metodun(init fonksiyonundan kasıt ve C#'da daha çok geçen isim yapıcı metottur) içindeki sayi1 ve sayi2 değerlerin,temeldeki yapıcı metot içinde yer alan sayi1 ve sayi2 değerlerinden temel(base) almasını sağlar--

    def OperationofMath(self):
        return math.sqrt(self.sayi1)



class Factorial(Mathematical):
    def __init__(self,sayi1,sayi2):
        super().__init__(sayi1,sayi2)

    def OperationofMath(self):
        return math.factorial(self.sayi2)



class Sub(Mathematical):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)

    def OperationofMath(self):
        return self.sayi1+self.sayi2


class Extraction(Mathematical):
    def __init__(self,sayi1,sayi2):
        super().__init__(sayi1,sayi2)

    def OperationofMath(self):
        return self.sayi1-self.sayi2


**Squart gibi yukarıdaki diğer gerçek matematiksel işlemler yapan sınıflarda da aynı işlemler geçerlidir**



class User:--Kullanıcımıza ait sınıf--

    def __init__(self,operation,sayi1,sayi2):
        self.operation=operation
        self.sayi1=sayi1
        self.sayi2=sayi2
       



    def DoTheOperation(self):
    --Burdaki metotta yapıcı metottan enjekte edilen operation nesnesinin OperationofMath metodunu döndürüyoruz.Bu metotun içindeki metot aynı zamanda genel matematik operasyon işlemlerini gerçekleştiren sınıfın metotudur ve bu vesileyle miras verdiği sınıflarda OperationofMath metotunu kullanabiliyor.--
        return self.operation.OperationofMath()







operation1=Squart(16,4) --Karekök sınıfı nesnesi--

operation2=Squart(25,16) --Karekök sınıfı nesnesi--

operation3=Factorial(4,5) --Faktöriyel sınıfı nesnesi--

operation4=Sub(4,3) --Toplama sınıfı nesnesi--

operation5=Extraction(11,5) --Çıkarma sınıfı nesnesi--

User=User(operation5,operation5.sayi1,operation5.sayi2) --Kullanıcı sınıfına ait nesne.Yapıcı metotu içinde üç tane değer enjekte edildiği ya da üç tane parametre konduğu için nesneyi oluştururken de parantez içinde üç tane değer aldı.Biri operasyon nesnesi ve diğer ikisi de operasyon nesnesinin sahip olduğu sayi1 ve sayi2 özellikleridir.--

sonuc=User.DoTheOperation()

print(sonuc)



