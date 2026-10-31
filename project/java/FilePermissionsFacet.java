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
  A file permissions facet is a grouping of characteristics unique to the access rights (e.g., view, change, navigate, execute) of a file on a file system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FilePermissionsFacet extends Facet {

  private UcoObject owner;


}