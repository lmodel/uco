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
  UcoType is the top-level class for metaclasses within UCO. An instance of core:UcoType is also an instance of owl:Class, and is or specializes core:UcoThing.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UcoType  {

  private URI id;
  private URI type;


}