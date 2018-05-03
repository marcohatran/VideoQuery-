package application;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.Scanner;


import javafx.beans.binding.Bindings;
import javafx.beans.property.DoubleProperty;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.media.MediaPlayer;
import javafx.scene.media.MediaView;
import javafx.scene.text.Text;
import javafx.util.Duration;
import javafx.scene.control.Slider;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextArea;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.media.Media;
import javafx.beans.*;


public class MainController implements Initializable {
	@FXML private MediaView mv;
	private MediaPlayer mp;
	private Media me;
	
	
	@FXML private MediaView mv2;
	private MediaPlayer mp2;
	private Media me2;
	
	@FXML private TableView<Ranking> ranking;
	@FXML private TableColumn<Ranking, Integer> rank;
	@FXML private TableColumn<Ranking, String> name;
	public ObservableList<Ranking> list = FXCollections.observableArrayList();
	@FXML private ImageView imageGraph;
	
//	@FXML private Slider timeSlider;
	
	
	String dbPathStub = "/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/databse_videos/";
	String qPathStub = "/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/query/";
	
	// CSV vars
	String[] vidNames = {"flowers", "interview", "movie", "musicvideo", "sports", "starcraft", "traffic"};
	double [] hist_vids_ranking = new double[7];
	double [] audio_vids_ranking = new double[7];
	private int vidIndex;					// Index for DB video start
	
	
	@Override
	public void initialize(URL location, ResourceBundle resources) {
		// TODO Auto-generated method stub
		String path = new File("src/media/first.mp4").getAbsolutePath();
		me = new Media(new File(path).toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
		
		//String path2 = new File(dbPathStub+"flowers/flowers.mp4").getAbsolutePath();
		me2 = new Media(new File(dbPathStub+"sports/sports.mp4").toURI().toString());
		mp2 = new MediaPlayer(me2);
		mv2.setMediaPlayer(mp2);
		
		
		
		//mp.setAutoPlay(true);
		/*
		DoubleProperty width = mv.fitWidthProperty();
		DoubleProperty height = mv.fitHeightProperty();
		width.bind(Bindings.selectDouble(mv.sceneProperty(), "width"));
		height.bind(Bindings.selectDouble(mv.sceneProperty(), "height"));
		*/
		
		//printRank();
		rank.setCellValueFactory(new PropertyValueFactory<Ranking, Integer>("rank"));
		name.setCellValueFactory(new PropertyValueFactory<Ranking, String>("name"));
		//list.sort(new SortByRank());
		//ranking.setItems(list);
		//csvReader();
		//createRankings();
		/*
		 * mp2.currentTimeProperty().addListener(new ChangeListener<Duration>() {
			@Override
			public void changed(ObservableValue<? extends Duration> observable, Duration oldValue, Duration newValue) {
				timeSlider.setValue(newValue.toSeconds());
			}
		});
		
		timeSlider.setOnMouseClicked(new EventHandler<MouseEvent>() {
			@Override
			public void handle (MouseEvent event) {
				mp2.seek(Duration.seconds(2));
			}
		});*/
		
		
	}
	
	public void play(ActionEvent event) {
		mp.setRate(1);
		mp2.setRate(1);
		mp.play();
		mp2.play();
	}
	public void pause(ActionEvent event) {
		mp.pause();
		mp2.pause();
	}
	public void fast(ActionEvent event) {
		mp.setRate(2);
		mp2.setRate(2);
	}
	public void slow(ActionEvent event) {
		mp.setRate(.5);
		mp2.setRate(.5);
	}
	public void reload(ActionEvent event) {
		mp.seek(mp.getStartTime());
		mp2.seek(mp2.getStartTime());
		mp.play();
		mp2.play();
	}
	public void start(ActionEvent event) {
		mp.seek(mp.getStartTime());
		mp2.seek(mp2.getStartTime());
		mp.stop();
		mp2.stop();
	}
	
	// ACTUALLY DOES AUDIO SORT NOW --- DO NOT CHANGE
	public void last(ActionEvent event) {
		/*mp.stop();
		mp2.stop();
		mp.seek(mp.getTotalDuration());		
		mp2.seek(mp2.getTotalDuration());*/
		createAudioRankings();
		printRankAudio();
	}
	public void first(ActionEvent event) {
		pythonQuery (1);
		//String path = new File("src/media/first.mp4").getAbsolutePath();
		me = new Media(new File(qPathStub + "first/first.mp4").toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
		//printRank();
	}
	public void second(ActionEvent event) {
		pythonQuery (2);
//		String path = new File(qPathStub + "second/second.mp4").getAbsolutePath();
		me = new Media(new File(qPathStub + "second/second.mp4").toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
		printRank();
	}
	public void q3(ActionEvent event) {
		pythonQuery (3);
//		String path = new File(qPathStub + "Q3/q3.mp4").getAbsolutePath();
		me = new Media(new File(qPathStub + "Q3/q3.mp4").toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
		printRank();
	}
	public void q4(ActionEvent event) {
		pythonQuery (4);
//		String path = new File(qPathStub + "Q4/q4.mp4").getAbsolutePath();
		me = new Media(new File(qPathStub + "Q4/q4.mp4").toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
		printRank();
	}
	public void q5(ActionEvent event) {
		pythonQuery (5);
//		String path = new File(qPathStub + "Q5/q5.mp4").getAbsolutePath();
		me = new Media(new File(qPathStub + "Q5/q5.mp4").toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
		printRank();
	}
	public void hq1(ActionEvent event) {
		pythonQuery (6);
//		String path = new File(qPathStub + "HQ1/hq1.mp4").getAbsolutePath();
		me = new Media(new File(qPathStub + "HQ1/hq1.mp4").toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
		printRank();
	}
	public void hq2(ActionEvent event) {
		pythonQuery (7);
//		String path = new File(qPathStub + "HQ2/hq2.mp4").getAbsolutePath();
		me = new Media(new File(qPathStub + "HQ2/hq2.mp4").toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
		printRank();
	}
	public void hq4(ActionEvent event) {
		pythonQuery (8);
//		String path = new File(qPathStub + "HQ4/hq4.mp4").getAbsolutePath();
		me = new Media(new File(qPathStub + "HQ4/hq4.mp4").toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
		printRank();
	}
	public void query(ActionEvent event) {
		pythonQuery (9);
//		String path = new File(qPathStub + "HQ3/hq3.mp4").getAbsolutePath();
		me = new Media(new File(qPathStub + "HQ3/hq3.mp4").toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
		printRank();
	}
	
	
	public void getResults(ActionEvent event) {
		csvReader();
	}
	
	public void dbVidLoader() {
		String dbVidName = list.get(0).getName() + "/" + list.get(0).getName() + ".mp4";
		long msSeek = (vidIndex / 600) * 20 *1000;
		me2 = new Media(new File(dbPathStub+dbVidName).toURI().toString());
		mp2 = new MediaPlayer(me2);
		mv2.setMediaPlayer(mp2);
		mp2.setStopTime(Duration.seconds(20));
		mp2.pause();
		mp2.setStartTime(Duration.millis(msSeek));
		System.out.println(mp2.getStartTime());
		mp2.seek(mp2.getStartTime().add(Duration.millis(msSeek)));
//		mp2.setStopTime(Duration.millis(13000));
//		mp2.setStartTime(Duration.seconds(3));


			
	}
	
	private void printRank() {
		list.sort(new SortByRank());
		ranking.setItems(list);
	}
	
	private void printRankAudio() {
		list.sort(new SortByRankRev());
		ranking.setItems(list);
	}
	
	private void addImage() {
		Image img = new Image(new File("/Users/taufeqrazakh/Desktop/CSProject/final576/MediaPlayerTest/CorrelationData.png").toURI().toString());
		imageGraph = new ImageView();
		imageGraph.setImage(img);
	}
	
	private void csvReader() {
		try {
			Scanner scanner = new Scanner(new File("/Users/taufeqrazakh/Desktop/CSProject/final576/MediaPlayerTest/results.csv"));
			scanner.useDelimiter(" ");
			int loopIndex = 1;
			int tmpIndex = 0;
	        while(scanner.hasNext()){
	            if (loopIndex == 3) {
	            	vidIndex = Integer.parseInt(scanner.nextLine());
	            }
	            else if (loopIndex >= 5 && loopIndex <= 11) {
	            	hist_vids_ranking[loopIndex - 5] = Double.parseDouble(scanner.nextLine());
	            }
	            else if (loopIndex >= 16 && loopIndex <= 22) {
	            	audio_vids_ranking[loopIndex - 16] = Double.parseDouble(scanner.nextLine());
//	            	System.out.println(scanner.nextLine());
	            }
	            else {
	            	scanner.nextLine();
	            }
	            loopIndex++;
	        }
	        scanner.close();
	        //System.out.println(vidIndex);
	        createRankings();
	        printRank();
	        dbVidLoader();
	        addImage();
		} 
		catch (FileNotFoundException e) {
            e.printStackTrace();
        }
	}
	
	private void createRankings() {
		list = FXCollections.observableArrayList();
		for (int i = 0; i < hist_vids_ranking.length; i ++) {
			list.add(new Ranking(hist_vids_ranking [i], vidNames[i]));
		}
	}
	
	private void createAudioRankings() {
		list = FXCollections.observableArrayList();
		for (int i = 0; i < audio_vids_ranking.length; i ++) {
			list.add(new Ranking(audio_vids_ranking [i], vidNames[i]));
		}
	}
	
	
	
	private void pythonQuery (int qNum) {
		String query = "/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/query/";
		if (qNum == 1) {
			query = query + "first/";
		}
		else if (qNum == 2) {
			query = query + "second/";
		}
		else if (qNum == 3) {
			query = query + "Q3/";
		}
		else if (qNum == 4) {
			query = query + "Q4/";
		}
		else if (qNum == 5) {
			query = query + "Q5/";
		}
		else if (qNum == 6) {
			query = query + "HQ1/";
		}
		else if (qNum == 7) {
			query = query + "HQ2/";
		}
		else if (qNum == 8) {
			query = query + "HQ4/";
		}
		/*
		else if (qNum == 9) {
			query = query + "HQ4/";
		}
		
		 * ADD FOR NEW FILE
		 * else if (qNum == 9) {
			query = query + "HQ4/";
		}*/
		String[] cmd = {"/usr/local/bin/python3", "/Users/taufeqrazakh/Desktop/CSProject/final576/Comparator.py", query};
		try {
			Runtime.getRuntime().exec(cmd);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
	}

}
