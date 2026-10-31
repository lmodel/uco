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
  A build utility type characterizes the tool used to convert from source code to executable code for a particular version of software.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BuildUtilityType extends UcoInherentCharacterizationThing {

  private String buildUtilityName;
  private String cpeid;
  private String swid;


}