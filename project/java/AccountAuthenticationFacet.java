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
  An account authentication facet is a grouping of characteristics unique to the mechanism of accessing an account.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AccountAuthenticationFacet extends Facet {

  private String password;
  private ZonedDateTime passwordLastChanged;
  private String passwordType;


}