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
  A process facet is a grouping of characteristics unique to an instance of a computer program executed on an operating system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProcessFacet extends Facet {

  private List<String> arguments;
  private ObservableObject binary;
  private ObservableObject creatorUser;
  private String currentWorkingDirectory;
  private Dictionary environmentVariables;
  private Integer exitStatus;
  private ZonedDateTime exitTime;
  private Boolean isHidden;
  private ZonedDateTime observableCreatedTime;
  private ObservableObject parent;
  private Integer pid;
  private String status;


}