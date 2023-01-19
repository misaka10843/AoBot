import fuz_pb2
from urllib.request import Request, urlopen

COOKIE = "is_logged_in=true; fuz_session_key="
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
" AppleWebKit/537.36 (KHTML, like Gecko)"
" Chrome/96.0.4664.55"
" Safari/537.36"
" Edg/96.0.1054.34"

API_HOST = "https://api.comic-fuz.com"
IMG_HOST = "https://img.comic-fuz.com"
TABLE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"
T_MAP = {s: i for i, s in enumerate(TABLE)}


def get_manga_index(mangaId: int, token: str) -> fuz_pb2.MangaViewerResponse:
    body = fuz_pb2.MangaDetailRequest()
    body.deviceInfo.deviceType = fuz_pb2.DeviceInfo.DeviceType.BROWSER
    body.chapterId = mangaId
    # body.viewerMode.imageQuality = fuz_pb2.ViewerMode.ImageQuality.HIGH
    with open("./body.protobuf", "wb") as f:
        f.write(body.SerializeToString())
    res = get_index("/v1/manga_detail", body.SerializeToString(), token)
    index = fuz_pb2.MangaViewerResponse()
    with open("./index.protobuf", "wb") as f:
        f.write(res)
    index.ParseFromString(res)


def get_index(path: str, body: str, token: str) -> str:
    url = API_HOST + path
    headers = {"user-agent": USER_AGENT}
    if token:
        headers["cookie"] = COOKIE + token
    req = Request(url, body, headers, method="POST")
    with urlopen(req) as r:
        return r.read()


def main():
    token = "2707c0028c158e0e1d7302237f86f18926e2a87b658eeb9243c9c46cabc0250f"
    get_manga_index(3152, token)


main()
