package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An SQLite blob facet is a grouping of characteristics unique to a blob (binary large object) of data within an SQLite database. [based on https://en.wikipedia.org/wiki/SQLite]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SQLiteBlobFacet extends Facet {

  private String columnName;
  private String rowCondition;
  private List<Integer> rowIndex;
  private String tableName;


}