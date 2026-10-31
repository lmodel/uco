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
  A digital signature info facet is a grouping of characteristics unique to a value calculated via a mathematical scheme for demonstrating the authenticity of an electronic message or document.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DigitalSignatureInfoFacet extends Facet {

  private Identity certificateIssuer;
  private UcoObject certificateSubject;
  private String signatureDescription;
  private Boolean signatureExists;
  private Boolean signatureVerified;


}