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
  UcoThing is the top-level class for individuals within UCO.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UcoThing  {

  private URI type;


}