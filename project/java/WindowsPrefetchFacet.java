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
  A Windows prefetch facet is a grouping of characteristics unique to entries in the Windows prefetch file (used to speed up application startup starting with Windows XP).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsPrefetchFacet extends Facet {

  private List<ObservableObject> accessedDirectory;
  private List<ObservableObject> accessedFile;
  private String applicationFileName;
  private ZonedDateTime firstRun;
  private ZonedDateTime lastRun;
  private String prefetchHash;
  private Integer timesExecuted;
  private ObservableObject volume;


}