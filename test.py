// paymentProcessor.js
class PaymentProcessor {
  /**
   * Calculates how much the organization actually receives from a credit card donation.
   * @param {number} amount - transaction amount (in dollars)
   * @param {boolean} coverFee - whether the donor opted to "cover the fee"
   * @returns {number} net amount that the nonprofit receives
   */
  static calculateNetAmount(amount, coverFee) {
    const flatFee = 0.3; // flat transaction fee
    const percentFee = 0.029; // 2.9% processing fee
    const fee = flatFee + amount * percentFee;
    if (coverFee) {
      const net = amount - fee;
      return net < 0 ? 0 : net;
    }
    return amount - fee;
  }
}
module.exports = PaymentProcessor;
