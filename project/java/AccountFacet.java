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
  An account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control the provision of some capability or service.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AccountFacet extends Facet {

  private String accountIdentifier;
  private UcoObject accountIssuer;
  private String accountType;
  private ZonedDateTime expirationTime;
  private Boolean isActive;
  private ZonedDateTime observableCreatedTime;
  private ZonedDateTime observableModifiedTime;
  private UcoObject owner;


}