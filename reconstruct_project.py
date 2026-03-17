from pathlib import Path
import shutil

root = Path(".")
files = {
    "root_build.gradle.kts": "build.gradle.kts",
    "app_build.gradle.kts": "app/build.gradle.kts",
    "app_proguard-rules.pro": "app/proguard-rules.pro",
    "app_AndroidManifest.xml": "app/src/main/AndroidManifest.xml",
    "app_MainActivity.kt": "app/src/main/java/no/adrgodspro/app/MainActivity.kt",
    "app_ScanActivity.kt": "app/src/main/java/no/adrgodspro/app/ScanActivity.kt",
    "app_index.html": "app/src/main/assets/www/index.html",
    "res_layout_activity_main.xml": "app/src/main/res/layout/activity_main.xml",
    "res_layout_activity_scan.xml": "app/src/main/res/layout/activity_scan.xml",
    "res_values_strings.xml": "app/src/main/res/values/strings.xml",
    "res_values_themes.xml": "app/src/main/res/values/themes.xml",
    "res_xml_backup_rules.xml": "app/src/main/res/xml/backup_rules.xml",
    "res_xml_data_extraction_rules.xml": "app/src/main/res/xml/data_extraction_rules.xml",
    "res_mipmap_anydpi_v26_ic_launcher.xml": "app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml",
    "res_mipmap_anydpi_v26_ic_launcher_round.xml": "app/src/main/res/mipmap-anydpi-v26/ic_launcher_round.xml",
}
for flat_name, dest_rel in files.items():
    src = root / flat_name
    dest = root / dest_rel
    if not src.exists():
        continue
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)

for dens in ["mdpi","hdpi","xhdpi","xxhdpi","xxxhdpi"]:
    for flat_base, out_name in [("ic_launcher", "ic_launcher.png"), ("ic_launcher_round", "ic_launcher_round.png")]:
        src = root / f"mipmap_{dens}_{flat_base}.png"
        dest = root / f"app/src/main/res/mipmap-{dens}/{out_name}"
        if not src.exists():
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

print("Project reconstructed.")
