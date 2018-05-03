package application;

import java.util.Comparator;

import javafx.beans.property.SimpleDoubleProperty;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;

public class Ranking {
	private final SimpleDoubleProperty rank;
	private final SimpleStringProperty name;
	
	public Ranking(Double rank, String name) {
		super();
		this.rank = new SimpleDoubleProperty(rank);
		this.name = new SimpleStringProperty(name);
	}

	public Double getRank() {
		return rank.get();
	}

	public String getName() {
		return name.get();
	}
}

class SortByRank implements Comparator<Ranking>
{
    // Used for sorting in ascending order of
    // roll number
    public int compare(Ranking a, Ranking b)
    {
    	double val = a.getRank() - b.getRank();
    	if (val > .00000000001) {
    		return -1;
    	}
    	else {
    		return 1;
    	}
         
    }
}
class SortByRankRev implements Comparator<Ranking>
{
    // Used for sorting in ascending order of
    // roll number
    public int compare(Ranking a, Ranking b)
    {
    	double val = a.getRank() - b.getRank();
    	if (val > .00000000001) {
    		return 1;
    	}
    	else {
    		return -1;
    	}
         
    }
}
