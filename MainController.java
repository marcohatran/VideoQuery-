package application;

import java.io.File;
import java.net.URL;
import java.util.ResourceBundle;

import javafx.beans.binding.Bindings;
import javafx.beans.property.DoubleProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.media.MediaPlayer;
import javafx.scene.media.MediaView;
import javafx.scene.text.Text;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextArea;
import javafx.scene.control.cell.PropertyValueFactory;
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
	public ObservableList<Ranking> list = FXCollections.observableArrayList(new Ranking(3, "music video"), new Ranking(1, "flowers"), new Ranking(2, "sports"));
	
	@Override
	public void initialize(URL location, ResourceBundle resources) {
		// TODO Auto-generated method stub
		String path = new File("src/media/first.mp4").getAbsolutePath();
		me = new Media(new File(path).toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
		
		String path2 = new File("src/media/interview.mp4").getAbsolutePath();
		me2 = new Media(new File(path2).toURI().toString());
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
		ranking.setItems(list);
		
		
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
	public void last(ActionEvent event) {
		mp.stop();
		mp2.stop();
		mp.seek(mp.getTotalDuration());		
		mp2.seek(mp2.getTotalDuration());
	}
	public void first(ActionEvent event) {
		String path = new File("src/media/first.mp4").getAbsolutePath();
		me = new Media(new File(path).toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
		list.sort(new SortByRank());
		ranking.setItems(list);
	}
	public void second(ActionEvent event) {
		String path = new File("src/media/flowers.mp4").getAbsolutePath();
		me = new Media(new File(path).toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
	}
	public void query(ActionEvent event) {
		String path = new File("src/media/interview.mp4").getAbsolutePath();
		me = new Media(new File(path).toURI().toString());
		mp = new MediaPlayer(me);
		mv.setMediaPlayer(mp);
	}
	
	private void printRank() {
		
	}

}
