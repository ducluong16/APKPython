from PyAPKDownloader.aptoide import Aptoide

# Tạo một mảng tập hợp các tên package_name
package_names = ["com.skype.raider", "com.viber.voip", "com.snapchat.android","com.whatsapp", "com.facebook.orca", "com.instagram.android", "com.twitter.android", "com.linkedin.android", "com.google.android.apps.plus", "com.google.android.apps.photos", "com.google.android.apps.maps", "com.google.android.youtube", "com.google.android.gm", "com.google.android.keep"]

# Tạo một đối tượng downloader
downloader = Aptoide()

# Download từng giá trị trong mảng package_names
for package_name in package_names:
    downloader.download_by_package_name(package_name=package_name)