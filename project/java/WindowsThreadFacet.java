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
  A Windows thread facet is a grouping os characteristics unique to a single thread of execution within a Windows process.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsThreadFacet extends Facet {

  private List<Integer> creationFlags;
  private ZonedDateTime creationTime;
  private ZonedDateTime observableCreatedTime;
  private String observableContext;
  private List<String> parameterAddress;
  private Integer priority;
  private String runningStatus;
  private String securityAttributes;
  private List<Integer> stackSize;
  private List<String> startAddress;
  private List<Integer> threadID;


}