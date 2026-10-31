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
  A configuration entry is a grouping of characteristics unique to a particular parameter or initial setting for the use of a tool, application, software, or other cyber object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ConfigurationEntry extends UcoInherentCharacterizationThing {

  private String itemDescription;
  private String itemName;
  private List<UcoObject> itemObject;
  private String itemType;
  private List<String> itemValue;


}