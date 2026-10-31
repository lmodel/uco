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
  A tool is an element of hardware and/or software utilized to carry out a particular function.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Tool extends UcoObject {

  private Identity creator;
  private List<URI> references;
  private String servicePack;
  private String toolType;
  private String version;


}