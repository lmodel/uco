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
  A database record facet contains properties associated with a specific table record value from a database.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TableFieldFacet extends Facet {

  private Boolean recordFieldIsNull;
  private String recordFieldName;
  private String recordFieldValue;
  private String recordRowID;
  private String tableName;
  private String tableSchema;


}