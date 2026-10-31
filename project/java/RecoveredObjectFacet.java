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
  Recoverability status of name, metadata, and content.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RecoveredObjectFacet extends Facet {

  private String contentRecoveredStatus;
  private String metadataRecoveredStatus;
  private String nameRecoveredStatus;


}