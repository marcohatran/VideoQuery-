package application;

import java.util.Comparator;

import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;

public class Ranking {
	private final SimpleIntegerProperty rank;
	private final SimpleStringProperty name;
	
	public Ranking(Integer rank, String name) {
		super();
		this.rank = new SimpleIntegerProperty(rank);
		this.name = new SimpleStringProperty(name);
	}

	public Integer getRank() {
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
        return a.getRank() - b.getRank();
    }
}
