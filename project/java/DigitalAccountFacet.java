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
  A digital account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control the provision of some capability or service within the digital domain.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DigitalAccountFacet extends Facet {

  private List<String> accountLogin;
  private String displayName;
  private ZonedDateTime firstLoginTime;
  private Boolean isDisabled;
  private ZonedDateTime lastLoginTime;


}