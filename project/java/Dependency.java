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
  A dependency is a grouping of characteristics unique to something that a tool or other software relies on to function as intended.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Dependency extends UcoInherentCharacterizationThing {

  private String dependencyDescription;
  private String dependencyType;


}