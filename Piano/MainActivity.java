//안드로이드 스튜디오 자바 코드

package com.rasp.piano;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;

public class MainActivity extends AppCompatActivity {
    Socket socket;
    OutputStream os;
    InputStream is;
    BufferedReader in;
    PrintWriter out;
    ConnectThread thread;

    Button btnConnect, btnDisConnect, DO, RE, MI, FA, SOL, RA, SI, DO_H;
    EditText edServerIP;
    TextView tvMessage;
    Handler handler = new Handler();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        tvMessage = (TextView) findViewById(R.id.tvMessage);
        btnConnect = (Button) findViewById(R.id.btnConnect);
        btnDisConnect = (Button) findViewById(R.id.btnDisconnect);
        DO = (Button)  findViewById(R.id.DO);
        RE = (Button)  findViewById(R.id.RE);
        MI = (Button)  findViewById(R.id.MI);
        FA = (Button)  findViewById(R.id.FA);
        SOL = (Button)  findViewById(R.id.SOL);
        RA = (Button)  findViewById(R.id.RA);
        SI = (Button)  findViewById(R.id.SI);
        DO_H = (Button)  findViewById(R.id.DO_H);
        edServerIP = (EditText) findViewById(R.id.edServerIP);

        btnConnect.setEnabled(true);
        btnDisConnect.setEnabled(false);
        DO.setEnabled(false);
        RE.setEnabled(false);
        MI.setEnabled(false);
        FA.setEnabled(false);
        SOL.setEnabled(false);
        RA.setEnabled(false);
        SI.setEnabled(false);
        DO_H.setEnabled(false);
        //서버와 연결하기 위한 버튼, 해당 버튼이 눌렸을 때 실행된다.
        btnConnect.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String addr = edServerIP.getText().toString().trim();
                /*해당 주로 서버를 연결하기 위해 입력된 주소를 좌우 공백을 제거하고
                ip주소를 저장한다.*/
                thread = new ConnectThread(addr);
                thread.start();

                btnConnect.setEnabled(false); 
                //서버가 연결되고나면 버튼의 필요성이 사라지므로 비활성화
                btnDisConnect.setEnabled(true);
                DO.setEnabled(true);
                RE.setEnabled(true);
                MI.setEnabled(true);
                FA.setEnabled(true);
                SOL.setEnabled(true);
                RA.setEnabled(true);
                SI.setEnabled(true);
                DO_H.setEnabled(true);
            }
        });
        btnDisConnect.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                thread.setStop();

                btnConnect.setEnabled(true);
                btnDisConnect.setEnabled(false);
            }
        });
        /*피아노 건반 버튼을 눌렀을 때 실행됨
        건반이 눌렸을 때 해당 계이름의 문자열을 서버로 보내기 위한 메소드*/
        DO.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                btnConnect.setEnabled(false);
                //모든 건반을 누를 수 있도록 버튼 활성화
                DO.setEnabled(true);
                RE.setEnabled(true);
                MI.setEnabled(true);
                FA.setEnabled(true);
                SOL.setEnabled(true);
                RA.setEnabled(true);
                SI.setEnabled(true);
                DO_H.setEnabled(true);
                btnDisConnect.setEnabled(true);

                new Thread(){
                    public void run(){
                        out.println("do");
                        //서버에서 문자열 비교해 계이름에 해당하는 주파수 신호를 출력하게 된다.
                        out.flush();
                        //버퍼가 꽉 차지 않아도 데이터를 보내기 위해 사용한다.
                        thread.readServer();
                    }
                }.start();
            }
        });
        RE.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                btnConnect.setEnabled(false);
                DO.setEnabled(true);
                RE.setEnabled(true);
                MI.setEnabled(true);
                FA.setEnabled(true);
                SOL.setEnabled(true);
                RA.setEnabled(true);
                SI.setEnabled(true);
                DO_H.setEnabled(true);
                btnDisConnect.setEnabled(true);

                new Thread(){
                    public void run(){
                        out.println("re");
                        out.flush();

                        thread.readServer();
                    }
                }.start();
            }
        });
        MI.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                btnConnect.setEnabled(false);
                DO.setEnabled(true);
                RE.setEnabled(true);
                MI.setEnabled(true);
                FA.setEnabled(true);
                SOL.setEnabled(true);
                RA.setEnabled(true);
                SI.setEnabled(true);
                DO_H.setEnabled(true);
                btnDisConnect.setEnabled(true);

                new Thread(){
                    public void run(){
                        out.println("mi");
                        out.flush();

                        thread.readServer();
                    }
                }.start();
            }
        });
        FA.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                btnConnect.setEnabled(false);
                DO.setEnabled(true);
                RE.setEnabled(true);
                MI.setEnabled(true);
                FA.setEnabled(true);
                SOL.setEnabled(true);
                RA.setEnabled(true);
                SI.setEnabled(true);
                DO_H.setEnabled(true);
                btnDisConnect.setEnabled(true);

                new Thread(){
                    public void run(){
                        out.println("fa");
                        out.flush();

                        thread.readServer();
                    }
                }.start();
            }
        });
        SOL.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                btnConnect.setEnabled(false);
                DO.setEnabled(true);
                RE.setEnabled(true);
                MI.setEnabled(true);
                FA.setEnabled(true);
                SOL.setEnabled(true);
                RA.setEnabled(true);
                SI.setEnabled(true);
                DO_H.setEnabled(true);
                btnDisConnect.setEnabled(true);

                new Thread(){
                    public void run(){
                        out.println("sol");
                        out.flush();

                        thread.readServer();
                    }
                }.start();
            }
        });
        RA.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                btnConnect.setEnabled(false);
                DO.setEnabled(true);
                RE.setEnabled(true);
                MI.setEnabled(true);
                FA.setEnabled(true);
                SOL.setEnabled(true);
                RA.setEnabled(true);
                SI.setEnabled(true);
                DO_H.setEnabled(true);
                btnDisConnect.setEnabled(true);

                new Thread(){
                    public void run(){
                        out.println("ra");
                        out.flush();

                        thread.readServer();
                    }
                }.start();
            }
        });
        SI.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                btnConnect.setEnabled(false);
                DO.setEnabled(true);
                RE.setEnabled(true);
                MI.setEnabled(true);
                FA.setEnabled(true);
                SOL.setEnabled(true);
                RA.setEnabled(true);
                SI.setEnabled(true);
                DO_H.setEnabled(true);
                btnDisConnect.setEnabled(true);

                new Thread(){
                    public void run(){
                        out.println("si");
                        out.flush();

                        thread.readServer();
                    }
                }.start();
            }
        });
        DO_H.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                btnConnect.setEnabled(false);
                DO.setEnabled(true);
                RE.setEnabled(true);
                MI.setEnabled(true);
                FA.setEnabled(true);
                SOL.setEnabled(true);
                RA.setEnabled(true);
                SI.setEnabled(true);
                DO_H.setEnabled(true);
                btnDisConnect.setEnabled(true);

                new Thread(){
                    public void run(){
                        out.println("hdo");
                        out.flush();

                        thread.readServer();
                    }
                }.start();
            }
        });
    }
    //서버와 연결해 데이터를 주고 받을 스레드를 상속받은 클래스
    class ConnectThread extends Thread{
        String hostname;
        public ConnectThread(String addr){
            hostname = addr; //ip주소 저장
        }

        public void run(){

            try {
                int port = 9018;
                socket = new Socket(hostname, port);
                //소켓을 생성해 hostname 주소에 포트 9018번으로 연결하는 클라이언트 소켓 생성
                os = socket.getOutputStream(); //데이터 전송을 위한 출력 스트림 생성
                is = socket.getInputStream(); //서버 데이터를 읽기 위한 스트림 생성
                in = new BufferedReader(new InputStreamReader(is)); //문자열 타입으로 받기 위해 사용
                out = new PrintWriter(os); //문자열 전송을 위해 사용
            } catch (IOException e) {
                e.printStackTrace();
            }

        }
        public void readServer(){
            try {
                String msg1 = in.readLine(); //버퍼를 이용해 읽어옴
                /* 서버에서 보낸 데이터를 읽어 저장, 보통 상태를 표시 할 때 사용한다.
                ex. LED 상태 : ON */
                handler.post(new Runnable() {
                    @Override
                    public void run() {
                        tvMessage.setText("버튼을 누르면 건반 소리가 납니다. ");
                    }
                });
            }catch (IOException e){
                e.printStackTrace();
            }
        }
        //소켓이 연결되어있다면 소켓을 닫기 위한 메소드
        public void setStop() { 
            if (socket.isConnected()){
                try {
                    socket.close();
                }catch (Exception e){
                    e.printStackTrace();
                }
            }
        }
    }
}
 