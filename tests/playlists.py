# coding: utf-8
# Copyright 2014 Globo.com Player authors. All rights reserved.
# Use of this source code is governed by a MIT License
# license that can be found in the LICENSE file.

from os.path import dirname, abspath, join

TEST_HOST = 'http://localhost:8112'

SIMPLE_PLAYLIST = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXTINF:5220,
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_START_NEGATIVE_OFFSET = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXT-X-START:TIME-OFFSET=-2.0
#EXTINF:5220,
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_START_PRECISE = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXT-X-START:TIME-OFFSET=10.5,PRECISE=YES
#EXTINF:5220,
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_FILENAME = abspath(
    join(dirname(__file__), 'playlists/simple-playlist.m3u8'))

SIMPLE_PLAYLIST_URI = TEST_HOST + '/simple.m3u8'
TIMEOUT_SIMPLE_PLAYLIST_URI = TEST_HOST + '/timeout_simple.m3u8'
REDIRECT_PLAYLIST_URI = TEST_HOST + '/path/to/redirect_me'


PLAYLIST_WITH_NON_INTEGER_DURATION = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220.5
#EXTINF:5220.5,
http://media.example.com/entire.ts
'''

SLIDING_WINDOW_PLAYLIST = '''
#EXTM3U
#EXT-X-TARGETDURATION:8
#EXT-X-MEDIA-SEQUENCE:2680

#EXTINF:8,
https://priv.example.com/fileSequence2680.ts
#EXTINF:8,
https://priv.example.com/fileSequence2681.ts
#EXTINF:8,
https://priv.example.com/fileSequence2682.ts
'''

PLAYLIST_WITH_ENCRIPTED_SEGMENTS = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7794
#EXT-X-TARGETDURATION:15

#EXT-X-KEY:METHOD=AES-128,URI="https://priv.example.com/key.php?r=52"

#EXTINF:15,
http://media.example.com/fileSequence52-1.ts
#EXTINF:15,
http://media.example.com/fileSequence52-2.ts
#EXTINF:15,
http://media.example.com/fileSequence52-3.ts
'''

VARIANT_PLAYLIST = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=1280000
http://example.com/low.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
http://example.com/mid.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000
http://example.com/hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,CODECS="mp4a.40.5,avc1.42801e"
http://example.com/audio-only.m3u8
'''

VARIANT_PLAYLIST_WITH_CC_SUBS_AND_AUDIO = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000,CLOSED-CAPTIONS="cc",SUBTITLES="sub",AUDIO="aud"
http://example.com/with-cc-hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,CLOSED-CAPTIONS="cc",SUBTITLES="sub",AUDIO="aud"
http://example.com/with-cc-low.m3u8
'''

VARIANT_PLAYLIST_WITH_VIDEO_CC_SUBS_AND_AUDIO = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000,CLOSED-CAPTIONS="cc",SUBTITLES="sub",AUDIO="aud",VIDEO="vid"
http://example.com/with-everything-hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,CLOSED-CAPTIONS="cc",SUBTITLES="sub",AUDIO="aud",VIDEO="vid"
http://example.com/with-everything-low.m3u8
'''

VARIANT_PLAYLIST_WITH_AVERAGE_BANDWIDTH = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1280000,AVERAGE-BANDWIDTH=1252345
http://example.com/low.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000,AVERAGE-BANDWIDTH=2466570
http://example.com/mid.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000,AVERAGE-BANDWIDTH=7560423
http://example.com/hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,AVERAGE-BANDWIDTH=63005,CODECS="mp4a.40.5,avc1.42801e"
http://example.com/audio-only.m3u8
'''

VARIANT_PLAYLIST_WITH_BANDWIDTH_FLOAT = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=1280000.0
http://example.com/low.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000.4
http://example.com/mid.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000.6
http://example.com/hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,CODECS="mp4a.40.5,avc1.42801e"
http://example.com/audio-only.m3u8
'''

VARIANT_PLAYLIST_WITH_IFRAME_PLAYLISTS = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=800000,RESOLUTION=624x352,CODECS="avc1.4d001f, mp4a.40.5"
video-800k.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1200000,CODECS="avc1.4d001f, mp4a.40.5"
video-1200k.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=400000,CODECS="avc1.4d001f, mp4a.40.5"
video-400k.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=150000,CODECS="avc1.4d001f, mp4a.40.5"
video-150k.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=64000,CODECS="mp4a.40.5"
video-64k.m3u8
#EXT-X-I-FRAME-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=151288,RESOLUTION=624x352,CODECS="avc1.4d001f",URI="video-800k-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=193350,CODECS="avc1.4d001f",URI="video-1200k-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=83598,CODECS="avc1.4d001f",URI="video-400k-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=38775,CODECS="avc1.4d001f",URI="video-150k-iframes.m3u8"
'''

VARIANT_PLAYLIST_WITH_ALT_IFRAME_PLAYLISTS_LAYOUT = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=800000,RESOLUTION=624x352,CODECS="avc1.4d001f, mp4a.40.5"
video-800k.m3u8
#EXT-X-I-FRAME-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=151288,RESOLUTION=624x352,CODECS="avc1.4d001f",URI="video-800k-iframes.m3u8"
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1200000,CODECS="avc1.4d001f, mp4a.40.5"
video-1200k.m3u8
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=193350,CODECS="avc1.4d001f",URI="video-1200k-iframes.m3u8"
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=400000,CODECS="avc1.4d001f, mp4a.40.5"
video-400k.m3u8
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=83598,CODECS="avc1.4d001f",URI="video-400k-iframes.m3u8"
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=150000,CODECS="avc1.4d001f, mp4a.40.5"
video-150k.m3u8
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=38775,CODECS="avc1.4d001f",URI="video-150k-iframes.m3u8"
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=64000,CODECS="mp4a.40.5"
video-64k.m3u8
'''

IFRAME_PLAYLIST = '''
#EXTM3U
#EXT-X-VERSION:4
#EXT-X-TARGETDURATION:10
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-I-FRAMES-ONLY
#EXTINF:4.12,
#EXT-X-BYTERANGE:9400@376
segment1.ts
#EXTINF:3.56,
#EXT-X-BYTERANGE:7144@47000
segment1.ts
#EXTINF:3.82,
#EXT-X-BYTERANGE:10340@1880
segment2.ts
#EXT-X-ENDLIST
'''

# reversing byterange and extinf from IFRAME.
IFRAME_PLAYLIST2 = '''
#EXTM3U
#EXT-X-VERSION:4
#EXT-X-TARGETDURATION:10
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-I-FRAMES-ONLY
#EXT-X-BYTERANGE:9400@376
#EXTINF:4.12,
segment1.ts
#EXT-X-BYTERANGE:7144@47000
#EXTINF:3.56,
segment1.ts
#EXT-X-BYTERANGE:10340@1880
#EXTINF:3.82,
segment2.ts
#EXT-X-ENDLIST
'''

PLAYLIST_USING_BYTERANGES = '''
#EXTM3U
#EXT-X-VERSION:4
#EXT-X-TARGETDURATION:11
#EXTINF:10,
#EXT-X-BYTERANGE:76242@0
segment.ts
#EXTINF:10,
#EXT-X-BYTERANGE:83442@762421
segment.ts
#EXTINF:10,
#EXT-X-BYTERANGE:69864@834421
segment.ts
#EXT-X-ENDLIST
'''

PLAYLIST_WITH_ENCRIPTED_SEGMENTS_AND_IV = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin", IV=0X10ef8f758ca555115584bb5b3c687f52
#EXT-X-TARGETDURATION:8
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_ENCRIPTED_SEGMENTS_AND_IV_SORTED = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:8
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin", IV=0X10ef8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_ENCRIPTED_SEGMENTS_AND_IV_WITH_MULTIPLE_KEYS = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin",IV=0X10ef8f758ca555115584bb5b3c687f52
#EXT-X-TARGETDURATION:8
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key2.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_ENCRIPTED_SEGMENTS_AND_IV_WITH_MULTIPLE_KEYS_SORTED = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:8
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin",IV=0X10ef8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key2.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_MULTIPLE_KEYS_UNENCRYPTED_AND_ENCRYPTED = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:8
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin",IV=0X10ef8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key2.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_MULTIPLE_KEYS_UNENCRYPTED_AND_ENCRYPTED_UPDATED = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:8
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key0.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin",IV=0X10ef8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key2.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_MULTIPLE_KEYS_UNENCRYPTED_AND_ENCRYPTED_NONE = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:8
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin",IV=0X10ef8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXT-X-KEY:METHOD=NONE,URI=""
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key2.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts

'''

PLAYLIST_WITH_MULTIPLE_KEYS_UNENCRYPTED_AND_ENCRYPTED_NONE_AND_NO_URI_ATTR = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:8
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin",IV=0X10ef8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXT-X-KEY:METHOD=NONE
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key2.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts

'''


SIMPLE_PLAYLIST_WITH_QUOTED_TITLE = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXTINF:5220,"A sample title"
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_UNQUOTED_TITLE = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXTINF:5220,A sample unquoted title
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_RESOLUTION = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=445000,RESOLUTION=512x288,CODECS="avc1.77.30, mp4a.40.5"
index_0_av.m3u8?e=b471643725c47acd
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=45000,CODECS="mp4a.40.5"
index_0_a.m3u8?e=b471643725c47acd
'''

SIMPLE_PLAYLIST_WITH_VOD_PLAYLIST_TYPE = '''
#EXTM3U
#EXT-X-PLAYLIST-TYPE:VOD
#EXTINF:180.00000,
some_video.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_INDEPENDENT_SEGMENTS = '''
#EXTM3U
#EXT-X-INDEPENDENT-SEGMENTS
#EXTINF:180.00000,
some_video.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_EVENT_PLAYLIST_TYPE = '''
#EXTM3U
#EXT-X-PLAYLIST-TYPE:EVENT
#EXTINF:180.00000,
some_video.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_PROGRAM_DATE_TIME = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:50116
#EXT-X-TARGETDURATION:3
#EXT-X-PROGRAM-DATE-TIME:2014-08-13T13:36:33+00:00
#EXTINF:3,
g_50116.ts
#EXTINF:3,
g_50117.ts
#EXTINF:3,
g_50118.ts
#EXTINF:3,
g_50119.ts
#EXTINF:3,
g_50120.ts
#EXTINF:3,
g_50121.ts
#EXTINF:3,
g_50122.ts
#EXTINF:3,
g_50123.ts

'''

# The playlist fails if parsed as strict, but otherwise passes
SIMPLE_PLAYLIST_MESSY = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXTINF:5220,
http://media.example.com/entire.ts
JUNK
#EXT-X-ENDLIST
'''

# The playlist fails if parsed as strict, but otherwise passes
SIMPLE_PLAYLIST_TITLE_COMMA = '''
#EXTM3U
#EXTINF:5220,Title with a comma, end
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

# Playlist with EXTINF record not ending with comma
SIMPLE_PLAYLIST_COMMALESS_EXTINF = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXTINF:5220
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

DISCONTINUITY_PLAYLIST_WITH_PROGRAM_DATE_TIME = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:50116
#EXT-X-TARGETDURATION:3
#EXT-X-PROGRAM-DATE-TIME:2014-08-13T13:36:33+00:00
#EXTINF:3,
g_50116.ts
#EXTINF:3,
g_50117.ts
#EXTINF:3,
g_50118.ts
#EXTINF:3,
g_50119.ts
#EXTINF:3,
g_50120.ts
#EXT-X-DISCONTINUITY
#EXT-X-PROGRAM-DATE-TIME:2014-08-13T13:36:55+00:00
#EXTINF:3,
g_50121.ts
#EXTINF:3,
g_50122.ts
#EXTINF:3,
g_50123.ts

'''

PLAYLIST_WITH_PROGRAM_DATE_TIME_WITHOUT_DISCONTINUITY = '''
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:6
#EXT-X-PLAYLIST-TYPE:EVENT
#EXT-X-MEDIA-SEQUENCE:50
#EXT-X-PROGRAM-DATE-TIME:2019-06-10T00:05:00.000Z
#EXTINF:6.000,
manifest_1_50.ts?m=1559946393
#EXT-X-PROGRAM-DATE-TIME:2019-06-10T00:05:06.000Z
#EXTINF:6.000,
manifest_1_51.ts?m=1559946393
#EXT-X-PROGRAM-DATE-TIME:2019-06-10T00:05:12.000Z
#EXTINF:6.000,
manifest_1_52.ts?m=1559946393
#EXT-X-ENDLIST
'''

CUE_OUT_PLAYLIST = '''
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:143474331
#EXT-X-VERSION:3
#EXTINF:10,
#EXT-X-PROGRAM-DATE-TIME:2015-06-18T23:22:10Z
1432451707508/ts/71737/sequence143474338.ts
#EXT-X-CUE-OUT-CONT:CAID=0x000000002310E3A8,ElapsedTime=161,Duration=181
#EXTINF:10,
#EXT-X-PROGRAM-DATE-TIME:2015-06-18T23:22:20Z
1432451707508/ts/71737/sequence143474339.ts
#EXT-X-CUE-OUT-CONT:CAID=0x000000002310E3A8,ElapsedTime=171,Duration=181
#EXTINF:10,
#EXT-X-PROGRAM-DATE-TIME:2015-06-18T23:22:30Z
1432451707508/ts/71737/sequence143474340.ts
#EXT-OATCLS-SCTE35:/DA5AAAAAAAA/wCABQb+aDhDgAAjAhdDVUVJQAAAV3+fCAgAAAAAIxDjqDUCAAAIQ1VFSQAAAABSV+PX
#EXT-X-CUE-IN
#EXTINF:10,
#EXT-X-PROGRAM-DATE-TIME:2015-06-18T23:22:40Z
1432451707508/ts/71737/sequence143474341.ts

'''

CUE_OUT_ELEMENTAL_PLAYLIST = '''
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:47224
#EXTINF:10.000,
master2500_47224.ts
#EXTINF:10.000,
master2500_47225.ts
#EXTINF:2.040,
master2500_47226.ts
#EXT-OATCLS-SCTE35:/DAlAAAAAAAAAP/wFAUAAAABf+//wpiQkv4ARKogAAEBAQAAQ6sodg==
#EXT-X-CUE-OUT:50.000
#EXTINF:7.960,
master2500_47227.ts
#EXT-X-CUE-OUT-CONT:ElapsedTime=7.960,Duration=50,SCTE35=/DAlAAAAAAAAAP/wFAUAAAABf+//wpiQkv4ARKogAAEBAQAAQ6sodg==
#EXTINF:10.000,
master2500_47228.ts
#EXT-X-CUE-OUT-CONT:ElapsedTime=17.960,Duration=50,SCTE35=/DAlAAAAAAAAAP/wFAUAAAABf+//wpiQkv4ARKogAAEBAQAAQ6sodg==
#EXTINF:10.000,
master2500_47229.ts
#EXT-X-CUE-OUT-CONT:ElapsedTime=27.960,Duration=50,SCTE35=/DAlAAAAAAAAAP/wFAUAAAABf+//wpiQkv4ARKogAAEBAQAAQ6sodg==
#EXTINF:10.000,
master2500_47230.ts
#EXT-X-CUE-OUT-CONT:ElapsedTime=37.960,Duration=50,SCTE35=/DAlAAAAAAAAAP/wFAUAAAABf+//wpiQkv4ARKogAAEBAQAAQ6sodg==
#EXTINF:10.000,
master2500_47231.ts
#EXT-X-CUE-OUT-CONT:ElapsedTime=47.960,Duration=50,SCTE35=/DAlAAAAAAAAAP/wFAUAAAABf+//wpiQkv4ARKogAAEBAQAAQ6sodg==
#EXTINF:2.040,
master2500_47232.ts
#EXT-X-CUE-IN
#EXTINF:7.960,
master2500_47233.ts
'''

CUE_OUT_ENVIVIO_PLAYLIST = '''
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:11
#EXT-X-MEDIA-SEQUENCE:399703
#EXTINF:10.0000,
20160914T080055-master804-199/1703.ts
#EXTINF:10.0000,
20160914T080055-master804-199/1704.ts
#EXTINF:5.1200,
20160914T080055-master804-199/1705.ts
#EXT-X-CUE-OUT:DURATION=366,ID=16777323,CUE="/DAlAAAENOOQAP/wFAUBAABrf+//N25XDf4B9p/gAAEBAQAAxKni9A=="
#EXTINF:10.0000,
20160914T080055-master804-199/1706.ts
#EXT-X-CUE-SPAN:TIMEFROMSIGNAL=PT10S,ID=16777323
#EXTINF:10.0000,
20160914T080055-master804-199/1707.ts
#EXT-X-CUE-SPAN:TIMEFROMSIGNAL=PT20S,ID=16777323
#EXTINF:10.0000,
20160914T080055-master804-199/1708.ts
#EXT-X-CUE-SPAN:TIMEFROMSIGNAL=PT30S,ID=16777323
#EXTINF:10.0000,
20160914T080055-master804-199/1709.ts
#EXT-X-CUE-IN:ID=16777323
#EXTINF:10.0000,
20160914T080055-master804-199/1710.ts
'''

MULTI_MEDIA_PLAYLIST = '''#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA:URI="chinese/ed.ttml",TYPE=SUBTITLES,GROUP-ID="subs",LANGUAGE="zho",NAME="Chinese",AUTOSELECT=YES,FORCED=NO
#EXT-X-MEDIA:URI="french/ed.ttml",TYPE=SUBTITLES,GROUP-ID="subs",LANGUAGE="fra",NAME="French",AUTOSELECT=YES,FORCED=NO
#EXT-X-MEDIA:URI="en/chunklist_w370587926_b160000_ao_slen_t64RW5nbGlzaA==.m3u8",TYPE=AUDIO,GROUP-ID="aac",LANGUAGE="en",NAME="English",DEFAULT=YES,AUTOSELECT=YES
#EXT-X-MEDIA:URI="sp/chunklist_w370587926_b160000_ao_slsp_t64U3BhbmlzaA==.m3u8",TYPE=AUDIO,GROUP-ID="aac",LANGUAGE="sp",NAME="Spanish",DEFAULT=NO,AUTOSELECT=YES
#EXT-X-MEDIA:URI="com/chunklist_w370587926_b160000_ao_slen_t64Q29tbWVudGFyeSAoZW5nKQ==.m3u8",TYPE=AUDIO,GROUP-ID="aac",LANGUAGE="en",NAME="Commentary (eng)",DEFAULT=NO,AUTOSELECT=NO
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2962000,RESOLUTION=1280x720,CODECS="avc1.66.30",AUDIO="aac",SUBTITLES="subs"
1280/chunklist_w370587926_b2962000_vo_slen_t64TWFpbg==.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1427000,RESOLUTION=768x432,CODECS="avc1.66.30",AUDIO="aac",SUBTITLES="subs"
768/chunklist_w370587926_b1427000_vo_slen_t64TWFpbg==.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=688000,RESOLUTION=448x252,CODECS="avc1.66.30",AUDIO="aac",SUBTITLES="subs"
448/chunklist_w370587926_b688000_vo_slen_t64TWFpbg==.m3u8
'''

MAP_URI_PLAYLIST = '''#EXTM3U
#EXT-X-TARGETDURATION:2
#EXT-X-VERSION:7
#EXT-X-MEDIA-SEQUENCE:1
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-INDEPENDENT-SEGMENTS
#EXT-X-MAP:URI="fileSequence0.mp4"
'''

MAP_URI_PLAYLIST_WITH_BYTERANGE = '''#EXTM3U
#EXT-X-TARGETDURATION:2
#EXT-X-VERSION:7
#EXT-X-MEDIA-SEQUENCE:1
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-INDEPENDENT-SEGMENTS
#EXT-X-MAP:URI="main.mp4",BYTERANGE="812@0"
'''

MEDIA_WITHOUT_URI_PLAYLIST = '''#EXTM3U
#EXT-X-VERSION:4
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-aacl-312",NAME="English",LANGUAGE="en",AUTOSELECT=YES,DEFAULT=YES,CHANNELS="2"
#EXT-X-STREAM-INF:BANDWIDTH=364000,AVERAGE-BANDWIDTH=331000,CODECS="mp4a.40.2",AUDIO="audio-aacl-312",SUBTITLES="textstream"
ch001-audio_312640_eng=312000.m3u8
'''

SIMPLE_PLAYLIST_WITH_DISCONTINUITY_SEQUENCE = '''#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXT-X-DISCONTINUITY-SEQUENCE:123
#EXTINF:5220,
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_CUSTOM_TAGS = '''#EXTM3U
#EXT-X-MOVIE: million dollar baby
#EXT-X-TARGETDURATION:5220
#EXTINF:5220,
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

RELATIVE_PLAYLIST_FILENAME = abspath(join(dirname(__file__), 'playlists/relative-playlist.m3u8'))

RELATIVE_PLAYLIST_URI = TEST_HOST + '/path/to/relative-playlist.m3u8'

CUE_OUT_PLAYLIST_FILENAME = abspath(join(dirname(__file__), 'playlists/cue_out.m3u8'))

CUE_OUT_PLAYLIST_URI = TEST_HOST + '/path/to/cue_out.m3u8'

VARIANT_PLAYLIST_WITH_FRAME_RATE = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1280000,FRAME-RATE=25
http://example.com/low.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000,FRAME-RATE=50
http://example.com/mid.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000,FRAME-RATE=60
http://example.com/hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,FRAME-RATE=12.5,CODECS="mp4a.40.5,avc1.42801e"
http://example.com/audio-only.m3u8
'''

del abspath, dirname, join
