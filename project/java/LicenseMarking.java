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
  A license marking is a grouping of characteristics unique to the expression of data marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of license restrictions that apply to the data.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LicenseMarking extends MarkingModel {

  private List<String> definitionType;
  private String license;


}