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
  A Windows process facet is a grouping of characteristics unique to a program running on a Windows operating system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsProcessFacet extends Facet {

  private Boolean aslrEnabled;
  private Boolean depEnabled;
  private String ownerSID;
  private String priority;
  private Dictionary startupInfo;
  private String windowTitle;


}