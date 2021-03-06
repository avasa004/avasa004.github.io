import java.net.*;
import java.io.*;
import java.util.*;
import java.text.DateFormat;


public class ProxyServer extends Thread{
	Socket s;
	PrintWriter writer;

	ProxyServer(Socket socket){
		this.s = socket;
	}

	public void run(){
		StringTokenizer st;
		try{

			InputStream istream = s.getInputStream();
			BufferedReader inLine = new BufferedReader(new InputStreamReader(istream));
			OutputStream ostream = s.getOutputStream();
			PrintStream pout = new PrintStream(ostream);

			String requestLine = inLine.readLine();
			// st = new StringTokenizer(requestLine);
			// String request = st.nextToken();
			// String uri = st.nextToken();
			
			// System.out.println("URL IS: " + uri);
			
			// URL url = new URL(request);
			// String host = url.getHost();
			// System.out.println("Host is: " + host);
			// int port = url.getPort();
			// System.out.println("Port is: " + port);
			// if(port == -1) port = 80;
			// String file = url.getFile();
			// System.out.println("File is: " + file);

			System.out.println("Received from Socket: " + requestLine);


		} catch(IOException ex){
			ex.printStackTrace();
		}
	}

	public static void main(String[] args) throws IOException{
		
		if(args.length != 2){
			System.out.println("Incorrect number of arguments");
			System.out.println("Usage: ProxyServer <config_file> <port_number>");
			return;
		}
		System.out.println("Starting ProxyServer on port " + args[1]);
		ServerSocket server = new ServerSocket (Integer.parseInt (args[1]));
		
		while(true){
			System.out.println("Listening for clients...");
			Socket client = server.accept();
			System.out.println("Accepted a connection from: " + client.getInetAddress());

			ProxyServer ps = new ProxyServer(client);
			ps.start();
		}
	}
}


