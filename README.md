<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://raw.githubusercontent.com/ubselcuk/spotify-cli/master/files/logo.gif" alt="Logo" width="250" height="250">
  </a>

  <h3 align="center">Spotify Command Line Interface</h3>
  <p align="center">
    <a href="https://github.com/ubselcuk/spotify-cli/issues">Hata Bildir</a>
    &
    <a href="https://github.com/ubselcuk/spotify-cli/issues">Request Feature</a>
  </p>
</p>










<details open="open">
  <summary><h2 style="display: inline-block">İçerik Tablosu</h2></summary>
  <ol>
    <li><a href="#proje-hakkında">Proje Hakkında</a></li>
    <li>
      <a href="#başlarken">Başlarken</a>
      <ul>
        <li><a href="#gereksinimler">Gereksinimler</a></li>
        <li><a href="#kurulum">Kurulum</a></li>
      </ul>
    </li>
    <li><a href="#kullanım">Kullanım</a></li>
    <li><a href="#lisans">Lisans</a></li>
    <li><a href="#teşekkürler">Teşekkürler</a></li>
  </ol>
</details>



## Proje Hakkında


Komut satırı arayüzünden basit komutlarla spotify kontrol etmenizi sağlayan bir komut satırı arayüzü.


## Başlarken
Bağlanmaya çalıştığınız spotify üyeliğiniz premium değilse büyük ihtimalle API çalışmayacaktır. Bu yüzden öncelikle premium hesabınız olduğundan emin olun.

Bu program spotify'ı terminalden kontrol etmenizi sağlar, sadece bu programı kullanarak müzik dinleyemezsiniz. Eğer bir daemon arıyorsanız [spotifyd](https://github.com/Spotifyd/spotifyd)'yi inceleyebilirsiniz. Komut satırından kullanabileceğiniz daha detaylı bir program arıyorsanız [spotify tui](https://github.com/Rigellute/spotify-tui)'ye bakabilirsiniz.

Telefondan veya spotify daemon gibi programlar üzerinden müzik dinliyorsanız bazı özellikler doğru olarak çalışmayabilir. Bu tür durumlarda [buradan](https://github.com/ubselcuk/spotify-cli/issues) bilgilendirirseniz dökümantasyona ekleyeceğim ve elimden geldiğince hataları çözmeye çalışacağım.


### Gereksinimler

Bilgisayarınızda python olması gerekiyor. Komut satırına ```python --version``` yazarak güncel python sürümünüzü öğrenebilirsiniz. Eğer python yüklemenize rağmen versiyonu göremiyorsanız path'e eklememiş olabilirsiniz. Bu proje python 3.9.5 ile yazıldı, daha eski sürümlerde çalışmayabilir.

Bazı gerekli kütüphaneleri indirmek için pip kullanacağız. Kuruluma geçmeden bilgisayarımızda pip var mı kontrol edeceğiz çünkü python 2.7.9+ ve python 3.4+ sürümlerinde python kurulumu ile beraber geliyor. Komut satırına ```pip --version``` yazarak güncel sürümünüzü öğrenebilirsiniz. Eğer yüklü değilse [pip](https://pip.pypa.io/en/stable/installation/) dökümantasyonunu takip ederek kurulum yapabilirsiniz.


Spotify API kullanabilmek için aşağıdaki bilgilere ihtiyacımız olacak.

* Client Id
* Client Secret
* Redirect Uri
* Spotify Username

Bu bilgileri nasıl elde edeceğinizi aşağıda adım adım açıklayacağım.

Hesabımızla [spotify developer](https://developer.spotify.com/)'a giriş yapıyoruz. Karşımıza şöyle bir ekran çıkacak.

-
Üst menüden dashboard'a tıklıyoruz. Bu şekilde bir ekran çıkıyor, kendi hesabımızla giriş yapıyoruz.

-

Giriş yaptıktan sonra create an app yazısına tıklıyoruz.


Oluşturacağımız uygulamanın adını ve açıklamasını girip create'ye basıyoruz. Bu adımda istediğiniz ismi verebilirsiniz.

Sol taraftan show client secret'e tıklıyoruz ve ihtiyacımız olan client id ve client secret değerlerine buradan ulaştık.

Daha sonra sağ üstten edit settings'e tıklıyoruz. Buradan Redirect uri'yi ayarlayacağız. [spotipy](https://spotipy.readthedocs.io/en/2.18.0/) dökümantasyonuna göre herhangi bir uri kullanabiliriz. Ben `http://localhost:8080` kullandım ancak siz bu uri'yi kullanmak zorunda değilsiniz. Değeri girdikten sonra add'e tıklıyoruz.

Dikkat! Eğer girdiğiniz uri bilgisayarınızda zaten kullanıyorsa program hata verecektir. Bu durumda farklı bir uri girmeniz gerekebilir. 

Son olarak [spotify](https://www.spotify.com/us/account/overview/)'a giriş yapıyoruz. Buradan kullanıcı adımızı öğreniyoruz.

[Bu](https://support.spotify.com/us/article/username-and-display-name/) linke göre spotify kullanıcı adı ve gösterilecek ad farklı şeyler. Eğer eski bir hesap kullanıyorsanız veya facebook'tan bağlanıyorsanız gösterilecek adınız ve kullanıcı adınız aynı olabilir ancak kontrol etmenizde fayda var.

Artık ihtiyacımız olan bütün bilgilere sahibiz. Kurulum aşamasında bu bilgileri kullanarak hesabımıza bağlanacağız.

### Kurulum

1. Github'dan projeyi klonlayın
   ```sh
   git clone https://github.com/ubselcuk/spotify-cli.git
   ```
2. Dosyanın olduğu dizine gidin
   ```sh
   cd spotify-cli
   ```
3. Gereksinimleri yükleyin
   ```sh
   pip install -r ???
   ```

#### Nedir bu cache?

#### Alias
hehe boi

## Kullanım

Önemli uyarı:
Bu andan itibaren komutlarda alias eklenildiğini varsayıp `sc` kullanacağım. Eğer alias eklemediyseniz komutları kullanırken aşağıdaki adımları takip etmeniz gerekmekte

- Dosyayı klonladığınız dizine gidin

```sh
  cd dosya/konumu
   ```

-  Komut vererek cli isimli python dosyasını çalıştırın, eğer herhangi bir komut vermezseniz uyarı verecektir.

```sh
  python3 cli.py help
```
Komut satırından komutları ve komutlar ile ilgili basit bilgilere bakmak için
```sh
   sc help
   sc h
   ```


Sonraki şarkıya geçmek için `next` veya `n` komutunu kullanabilirsiniz.

```sh
   sc next
   sc n
   ```

Önceki şarkıya geri dönmek için `prev`, `back` veya `b` komutunu kullanabilirsiniz.

```sh
   sc prev
   sc back
   sc b
   ```

Aktif olan cihazı ve kullanıcıyı göstermek için `device`, `devices` veya `d` komutunu kullanabilirsiniz.

```sh
   sc devices
   sc device
   sc d
   ```

Müziği tekrarlamak için `repeat` veya `r` komutunu kullanabilirsiniz ancak tekrarlama seçeneğini de belirtmeniz gerekiyor. 3 farklı seçim yapabilirsiniz.

- track - şarkıyı döngüye almak için
- context - şu anda çaldığınız listeyi döngüye almak için
- off - döngüleri kapatmak için

Bu seçeneklerden aynı anda sadece bir tanesi aktif oluyor, örneğin önce `track` daha sonra `context` komutu kullandığınızda şarkıyı dömgüye alma seçiminiz iptal oluyor.

```sh
   sc repeat track
   sc repeat context
   sc repeat off
   sc r off
   ```

Müziğin ses seviyesini ayarlamak için `volume` veya `v` komutunu kullanabilirsiniz. Eğer ses seviyesini belirtmezseniz şu anki ses seviyesini gösterir.

```sh
   sc volume
   sc v
   ```

Eğer ses seviyesini değiştirmek istiyorsanız `volume` veya `v` komutundan sonra `1` ile `100` aralığında istediğiniz değeri seçebilirsiniz. Aralığın dışındaki değerler hata verecektir.

```sh
   sc volume 42
   sc v 42
   ```

Şu anda çalan şarkıyı ve sanatçıyı görmek için `now playing` veya `np` komutunu kullanabilirsiniz.

```sh
   sc now playing
   sc np
   ```

Çalan şarkıyı durdurmak için `pause`, `stop` veya `s` komutunu kullanabilirsiniz. Eğer şarkı çalmıyorsa bir uyarı mesajı gösterecektir.

```sh
   sc pause
   sc stop
   sc s
   ```

Durmuş olan şarkıyı başlatmak için `start`, `play` veya `p` komutunu kullanabilirsiniz. Eğer şarkı çalıyorsa bir uyarı mesajı gösterecektir. Sıkça karşılaşılan bir sorun olarak, spotify daemon ilk açıldığında herhangi bir şarkı belirtilmemişse hata verebiliyor.  

```sh
   sc start
   sc play
   sc p
   ```

Girmiş olduğunuz bilgileri göstermek için `current user` veya `cu` komutunu kullanabilirsiniz. Bu komutun gösterdiği bilgiler aşağıda sıralanmıştır.

- Client Id
- Client Secret
- Redirect Uri
- Username


## Lisans
aa
## Teşekkürler

Geliştirme testlerine katılanlar


Bu dökümantasyon en son 00000 tarihinde güncellenmiştir.


#### TODO

search - play


```
history   List your recently played tracks.
```
```
Save a track, album, artist, or playlist.
```
```
seek      Seek to time (default unit: seconds) in the current track.
```

```
$ spotify status -vv
Track   Nights (03:31 / 05:07)
Artist  Frank Ocean
Album   Blonde
Status  Playing (on repeat, 60% volume)
```

```
spotify search red velvet

Search results for "red velvet"

  #  Track                                      Artist
---  -----------------------------------------  ---------------------------
  1  Psycho                                     Red Velvet
  2  Monster                                    Red Velvet - IRENE & SEULGI
  3  Bad Boy                                    Red Velvet

```

image url's
