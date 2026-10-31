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
  A user account facet is a grouping of characteristics unique to an account controlling a user's access to a network, system, or platform.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UserAccountFacet extends Facet {

  private Boolean canEscalatePrivs;
  private String homeDirectory;
  private Boolean isPrivileged;
  private Boolean isServiceAccount;


}