from __future__ import annotations

from typing import Optional


def build_request(host: str, path: str) -> bytes:
    """
    HTTP GET 요청 메시지를 바이트 형태로 생성합니다.
    """
    if not path.startswith("/"):
        path = "/" + path

    ###########################################################
    # TODO: HTTP/1.1 규격에 맞게 요청 문자열(GET, Host, Connection 헤더 포함)을 완성하세요.
    # HINT: 각 줄의 끝은 \r\n이며, 헤더의 끝에는 빈 줄(\r\n)이 하나 더 필요합니다.

    # HTTP/1.1 규격에 맞게 요청 문자열을 구성합니다.
    # 1. 요청 라인: GET {path} HTTP/1.1
    # 2. Host 헤더: 필수 포함 항목
    # 3. Connection: close 헤더: 응답 후 연결 종료를 위해 필요
    # 4. 각 줄은 \r\n으로 끝나야 하며, 마지막에 빈 줄(\r\n)이 추가되어야 함

    req = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"Connection: close\r\n"
        "\r\n"
    )
    
    ###########################################################

    return req.encode("utf-8")


def send_and_recv(sock, request: bytes, max_bytes: int) -> bytes:
    
    sock.sendall(request)

    chunks: list[bytes] = []
    total = 0
    while True:
        data = sock.recv(4096)
        if not data:
            break
        chunks.append(data)
        total += len(data)
        if total > max_bytes:
            break
    return b"".join(chunks)


def parse_status_and_preview(raw: bytes, max_preview: int = 200) -> tuple[Optional[int], str, Optional[str]]:
    """
    서버의 Raw 응답 데이터를 분석하여 상태 코드와 본문 미리보기를 추출합니다. 
    
    요구사항:
    1. 헤더와 바디를 구분하는 CRLF 2번(b"\\r\\n\\r\\n")의 위치를 찾으세요. 
    2. 헤더 영역을 decode한 뒤, Status Line(첫 줄)에서 상태 코드를 추출하세요. 
    3. 바디 영역에서 max_preview 만큼의 데이터를 decode하여 반환하세요. 
    4. 규격에 맞지 않는 데이터가 들어올 경우 적절한 에러 메시지를 반환하세요. 
    """
    
    ###########################################################
    # TODO: HTTP 응답 파싱 로직 전체를 직접 구현하세요.
    # 1. b"\r\n\r\n"를 기준으로 헤더와 바디를 분리합니다.
    # 2. 첫 줄(Status Line)에서 상태 코드(int)를 추출합니다. 
    # 3. 바디 영역을 max_preview 만큼 decode하여 preview를 만듭니다. 

    # HINT 1: raw.find(b"\\r\\n\\r\\n")으로 헤더와 바디의 경계를 나눕니다.
    # HINT 2: header.split("\\r\\n")의 첫 번째 줄을 다시 공백으로 split하면 상태 코드를 찾을 수 있습니다.

    status_code = None
    preview = ""
    error = None

    # 1. b"\r\n\r\n"를 기준으로 헤더와 바디를 분리합니다.
    header_end_idx = raw.find(b"\r\n\r\n")
    if header_end_idx == -1:
        return None, "", "Invalid HTTP response: Header separator not found"

    header_raw = raw[:header_end_idx]
    body_raw = raw[header_end_idx + 4:]

    try:
        # 2. 헤더 영역을 decode하고 Status Line에서 상태 코드를 추출합니다.
        header_text = header_raw.decode("utf-8")
        lines = header_text.split("\r\n")
        if not lines:
            return None, "", "Invalid HTTP response: Empty header"

        # Status Line 예시: "HTTP/1.1 200 OK"
        status_line = lines[0]
        status_parts = status_line.split()

        if len(status_parts) >= 2:
            try:
                status_code = int(status_parts[1])  # 두 번째 요소가 상태 코드입니다.
            except ValueError:
                error = "Invalid status code format"
        else:
            error = "Invalid status line format"

        # 3. 바디 영역을 max_preview 만큼 decode하여 preview를 만듭니다.
        preview = body_raw[:max_preview].decode("utf-8", errors="replace")

    except Exception as e:
        error = f"Parsing error: {str(e)}"

    ###########################################################
    
    return status_code, preview, error