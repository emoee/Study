// 서버에서 실행해야하는 코드

#include <wiringPi.h>
#include <softTone.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

#define PORT 9018
#define BUZZER_PIN 4
// 7음계에서 각 음에 해당하는 주파수 값 정의
#define DO 523
#define RE 587
#define MI 659
#define FA 698
#define SOL 784
#define RA 880 
#define SI 987 
#define DO_H 1046

int sevenScale(int scale){ //해당 숫자값이 넘어오면 해당 음에 해당하는 주파수 값을 반환한다.
    int _ret = 0;
    switch(scale){
    case 0: _ret = DO; break;
    case 1: _ret = RE; break;
    case 2: _ret = MI; break;
    case 3: _ret = FA; break;
    case 4: _ret = SOL; break;
    case 5: _ret = RA; break;
    case 6: _ret = SI; break;
    case 7: _ret = DO_H; break;
    }
    return _ret;
}
int main(void){
    if(wiringPiSetupGpio() == -1)
        return 1;
   
   softToneCreate(BUZZER_PIN);
   int s_socket, c_socket;
   //s소켓 : 클라이언트 연결 요청 처리 소켓, c소켓 : 연결된 클라이언트와 직접 통신할 소켓
   struct sockaddr_in s_addr, c_addr;

   int n;
   int len;
   char rcvBuffer[BUFSIZ];
   //클라이언트가 보내준 데이터 저장
   s_socket = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
   //클라이언트 연결 요청을 처리할 소켓을 생성한다.
   memset(&s_addr, 0, sizeof(s_addr)); //연결 요청을 수신할 주소를 설정해준다.
   s_addr.sin_addr.s_addr = htonl(INADDR_ANY); //네트워크 바이트 순서로 바꿔 저장
   s_addr.sin_family = AF_INET; // TCP/IP 통신
   s_addr.sin_port = htons(PORT); //9018포트에 연결된 프로그램 요청

    if(bind(s_socket, (struct sockaddr*)&s_addr, sizeof(s_addr)) == 1){
      printf("Can not bind\n");
      return 1;
   } //s소켓을 IP주소와 port번호에 연결한다.

   if(listen(s_socket, 5) == -1){
      printf("Listen fail\n");
      return 1;
   } //클라이언트 요청을 받을 수 있도록 수신 대기열을 생성해준다.

   printf("Echo Server started...\n");
    while(1){
      len = sizeof(c_addr);
      c_socket = accept(s_socket, (struct sockaddr*)&c_addr, &len);
      //s소켓으로 오는 연결 요청 중 c_addr주소는 c소켓이 처리한다.
      printf("Connected IP : %s\n", inet_ntoa(c_addr.sin_addr));
      //10진수 형태로 연결된 클라이언트 IP주소를 출력
      while((n = read(c_socket, rcvBuffer, sizeof(rcvBuffer)))>0){
         //c소켓을 통해 rcvBuffer를 이용해 데이터를 수신한다.
         rcvBuffer[n] = '\0'; //문장의 끝에 Null을 삽입한다.
         //if문을 통해 해당 계이름을 찾아서 주파수 신호를 출력해준다.
            if(strncmp(rcvBuffer, "do", 2) == 0){ //버퍼값과 계이름 비교
            printf("%s", rcvBuffer);
            softToneWrite(BUZZER_PIN, sevenScale(0)); //주파수 신호를 출력한다.
            delay(300); //0.3초 지연
            softToneWrite(BUZZER_PIN, 0); //정지
         }else if(strncmp(rcvBuffer, "re", 2) == 0){ //위와 동일
            printf("%s", rcvBuffer);
            softToneWrite(BUZZER_PIN, sevenScale(1));
            delay(300);
            softToneWrite(BUZZER_PIN, 0);
         }else if(strncmp(rcvBuffer, "mi", 2) == 0){
            printf("%s", rcvBuffer);
            softToneWrite(BUZZER_PIN, sevenScale(2));
            delay(300);
            softToneWrite(BUZZER_PIN, 0);
         }else if(strncmp(rcvBuffer, "fa", 2) == 0){
            printf("%s", rcvBuffer);
            softToneWrite(BUZZER_PIN, sevenScale(3));
            delay(300);
            softToneWrite(BUZZER_PIN, 0);
         }else if(strncmp(rcvBuffer, "sol", 3) == 0){
            printf("%s", rcvBuffer);
            softToneWrite(BUZZER_PIN, sevenScale(4));
            delay(300);
            softToneWrite(BUZZER_PIN, 0);
         }else if(strncmp(rcvBuffer, "ra", 2) == 0){
            printf("%s", rcvBuffer);
            softToneWrite(BUZZER_PIN, sevenScale(5));
            delay(300);
            softToneWrite(BUZZER_PIN, 0);
         }else if(strncmp(rcvBuffer, "si", 2) == 0){
            printf("%s", rcvBuffer);
            softToneWrite(BUZZER_PIN, sevenScale(6));
            delay(300);
            softToneWrite(BUZZER_PIN, 0);
         }else if(strncmp(rcvBuffer, "hdo", 3) == 0){
            printf("%s", rcvBuffer);
            softToneWrite(BUZZER_PIN, sevenScale(7));
            delay(300);
            softToneWrite(BUZZER_PIN, 0);
            /*계이름을 찾아 주파수 신호를 출력하고 난 후 해당 계이름을
            클라이언트 소켓에 전송 rcvBuffer내용을 전송한다. */
         }
         write(c_socket, rcvBuffer, n); //클라이언트와 연결 종료
      }
      close(c_socket); //서버 종료
   }
   close(s_socket);
   return 0;
}