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
  A library type is a grouping of characteristics unique to a collection of resources incorporated into the build of a software.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LibraryType extends UcoInherentCharacterizationThing {

  private String libraryName;
  private String libraryVersion;


}