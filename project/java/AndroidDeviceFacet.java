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
  An Android device facet is a grouping of characteristics unique to an Android device. [based on https://en.wikipedia.org/wiki/Android_(operating_system)]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AndroidDeviceFacet extends Facet {

  private String androidFingerprint;
  private String androidID;
  private String androidVersion;
  private Boolean isADBRootEnabled;
  private Boolean isSURootEnabled;


}